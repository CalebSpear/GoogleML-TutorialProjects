# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 21:10:30 2020

@author: caleb
"""

import os
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from keras.wrappers.scikit_learn import KerasRegressor 

os.chdir("/Users/vcben/Downloads")
names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year"
         , "origin", "car_name"]
data = pd.read_csv("auto-mpg.data", header=None,delimiter="\s+", skipinitialspace=True,
                   names=names, na_values=["?"])
data[data.isna().any(axis=1)]
m = 0
add = 0
length = 0
for i in data.horsepower:
    if not data.isna().horsepower[m]:
        add += data.horsepower[m]
        length += 1
    m+=1
data.horsepower = data.horsepower.fillna(int(add/length))
data[data.isna().any(axis=1)]
data.isna().any()
data.car_name.value_counts()

std_scale = StandardScaler().fit(data[['cylinders','displacement', 'horsepower', 'weight', 'acceleration',"model_year","origin"]])
data_std = std_scale.transform(data[['cylinders','displacement', 'horsepower', 'weight', 'acceleration',"model_year","origin"]])
data.cylinders = data_std[:,0]
data.displacement = data_std[:,1]
data.horsepower = data_std[:,2]
data.weight = data_std[:,3]
data.acceleration = data_std[:,4]
data.model_year = data_std[:,5]
data.origin = data_std[:,6]

X = data.drop(columns=["mpg", "car_name"]).values
Y = data["mpg"].values.flatten()

def wider_model():
    model = Sequential()
    model.add(Dense(20, input_dim=7, kernel_initializer='normal', activation='relu'))
    model.add(Dense(7, activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasRegressor(build_fn=wider_model, epochs=100, batch_size=5, verbose=1)))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10)
results = cross_val_score(pipeline, X, Y, cv=kfold)
print("Wider: %.2f (%.2f) MSE" % (results.mean(), results.std()))