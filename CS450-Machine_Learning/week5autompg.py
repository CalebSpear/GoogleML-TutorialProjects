# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 20:10:19 2020

@author: caleb
"""

import os
import graphviz 
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

os.chdir("/Users/caleb/Downloads")

names = ["mpg","cylinders","displacement","horsepower","weight","acceleration",
         "model_year","origin","car_name"]
         
data = pd.read_csv("autompg.data", header=None, delimiter= '\s+', skipinitialspace=True,
                   names=names, na_values=["?"])

add = 0
length = 0
for i in range(len(data.horsepower)):
    if not data.isnull().horsepower[i]:
        add += data.horsepower[i]
        length += 1
    
data.horsepower = data.horsepower.fillna(int(add/length))

data[data.isnull().any(axis=1)]
#print(data.isnull().any())

# Car Name- Label
#data.car_name.value_counts()
#data.car_name = data.car_name.astype('category')
#data["car_name_cat"] = data.car_name.cat.codes
#print(data.car_name_cat)
    
std_scale = StandardScaler().fit(data[['cylinders','displacement', 'horsepower', 'weight', 'acceleration',"model_year","origin"]])
data_std = std_scale.transform(data[['cylinders','displacement', 'horsepower', 'weight', 'acceleration',"model_year","origin"]])
data.cylinders = data_std[:,0]
data.displacement = data_std[:,1]
data.horsepower = data_std[:,2]
data.weight = data_std[:,3]
data.acceleration = data_std[:,4]
data.model_year = data_std[:,5]
data.origin = data_std[:,6]

# Car Name- One Hot
data.car_name.value_counts()
data = pd.get_dummies(data, columns=["car_name"])

X = data.drop(["mpg"],axis = 1).values
y = data["mpg"].values.flatten()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

regr = tree.DecisionTreeRegressor(max_depth = 6)

regr.fit(X_train, y_train)

y_pred = regr.predict(X_test)

per_error = 0
length = 0
for i in range(len(y_test)):
    if y_test[i] != 0:
        per_error += (abs(y_test[i] - y_pred[i]))/y_test[i]
        length += 1
        
mean_per_error = per_error/length
print("Final Grade Mean Percent Error: {}".format(mean_per_error))

error = mean_squared_error(y_test, y_pred)
#print(y_pred,"\n",y_test)
print("Final Grade Mean Squared Error: {}".format(error))

dot_data = tree.export_graphviz(regr, out_file=None, 
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  
graph.render("autompg") 