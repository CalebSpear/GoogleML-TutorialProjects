# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:09:00 2020

@author: caleb
"""

#print(clf.predict_proba([[2., 2.]]))
import os
import graphviz 
import pandas as pd
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

os.chdir("/Users/caleb/OneDrive/Documents/CS450")

names = ["type","plots","star","profit"]
         
data = pd.read_csv("dtreetestdata.csv", header=None, skipinitialspace=True,
                   names=names, na_values=["?"])

data.type.value_counts()
data["isComedy"] = data.type.map({"Comedy": 1, "Drama": 0})

data.plots.value_counts()
data["isDeep"] = data.plots.map({"Deep": 1, "Shallow": 0})

data.star.value_counts()
data["isYes"] = data.star.map({"Yes": 1, "No": 0})

data.profit.value_counts()
data["isLow"] = data.profit.map({"Low": 1, "High": 0})

data = data.drop(columns=["type","plots","star","profit"])

X = data.drop(["isLow"],axis = 1).values
y = data["isLow"].values.flatten()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = tree.DecisionTreeClassifier()
clf1 = clf.fit(X,y)

#y_pred = clf.predict(X_test)
#accuracy = accuracy_score(y_test, y_pred)
#print("Accuracy for Car Data: {}".format(accuracy))
#tree.plot_tree(clf.fit(X, y))
dot_data = tree.export_graphviz(clf, out_file=None, 
                     feature_names=["type","plots","star"],  
                     class_names=["Low","High"],  
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  
graph.render("profit") 
