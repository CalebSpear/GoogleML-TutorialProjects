# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 21:07:27 2020

@author: caleb
"""

from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import os
os.chdir("/Users/caleb/Downloads")
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')

X = dataset[:,0:8]
y = dataset[:,8]

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu')) 
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, epochs=150, batch_size=10)

_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))





