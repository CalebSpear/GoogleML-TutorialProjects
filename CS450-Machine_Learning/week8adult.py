# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 21:16:39 2020

@author: caleb
"""


from keras.models import Sequential
from keras.layers import Dense
import os
import pandas as pd

os.chdir("/Users/vcben/Downloads")
names = ["age", "workclass", "fnlwgt", "education", "education-num", "marital_status", "occupation"
         ,"relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native_country", "income"]
data = pd.read_csv("adult.data", header=None, skipinitialspace=True,
                   names=names, na_values=["?"])

data[data.isnull().any(axis=1)]
data.isnull().any()
data.workclass = data.workclass.fillna("unknown")
data.native_country = data.native_country.fillna("unknown")
data.occupation = data.occupation.fillna("unknown")
data[data.isnull().any(axis=1)]
data.isnull().any()

#these two lines are for label encoding
data.workclass = data.workclass.astype('category')
data["workclass_cat"] = data.workclass.cat.codes

data.education.value_counts()
data.education = data.education.astype('category')
data["education_cat"]= data.education.cat.codes

data.marital_status.value_counts()
data.marital_status = data.marital_status.astype('category')
data["marital_status_cat"]= data.marital_status.cat.codes

data.occupation.value_counts()
data.occupation = data.occupation.astype('category')
data["occupation_cat"]= data.occupation.cat.codes

data.relationship.value_counts()
data.relationship = data.relationship.astype('category')
data["relationship_cat"]= data.relationship.cat.codes

#this is one hot encoding
data = pd.get_dummies(data, columns=["race"])

#this is a binary mapping
data["isMale"] = data.sex.map({"Male": 1, "Female": 0})

data.native_country.value_counts()
data.native_country = data.native_country.astype('category')
data["native_country_cat"]= data.native_country.cat.codes

data.income.value_counts()
data["incomeHigh"] = data.income.map({">50K": 1, "<=50K": 0})
data = data.drop(["workclass", "education", "marital_status", "occupation",
                   "relationship", "sex", "native_country", "income"],axis = 1)

X = data.drop(["incomeHigh"],axis = 1).values
y = data["incomeHigh"].values.flatten()

model = Sequential()

model.add(Dense(12, input_dim=18, activation='relu'))
model.add(Dense(18, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=20, batch_size=50)

_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
