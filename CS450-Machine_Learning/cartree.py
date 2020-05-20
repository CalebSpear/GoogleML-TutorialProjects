# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:21:45 2020

@author: caleb
"""
import os
import graphviz 
import pandas as pd
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

os.chdir("/Users/caleb/Downloads")

names = ["buying","maint","doors","persons","lug_boot","safety","classes"]
         
data = pd.read_csv("car.data", header=None, skipinitialspace=True,
                   names=names, na_values=["?"])

data[data.isnull().any(axis=1)]
#print(data.isnull().any())

# Buying
data.buying.value_counts()
data.buying = data.buying.astype('category')
data["buying_cat"] = data.buying.cat.codes

# Maint
data.maint.value_counts()
data.maint = data.maint.astype('category')
data["maint_cat"] = data.maint.cat.codes

# Doors
data.doors.value_counts()
data.doors = data.doors.astype('category')
data["doors_cat"] = data.doors.cat.codes

# Persons
data.persons.value_counts()
data.persons = data.persons.astype('category')
data["persons_cat"] = data.persons.cat.codes

# Lug Boot
data.lug_boot.value_counts()
data.lug_boot = data.lug_boot.astype('category')
data["lug_boot_cat"] = data.lug_boot.cat.codes

# Safety
data.safety.value_counts()
data.safety = data.safety.astype('category')
data["safety_cat"] = data.safety.cat.codes

# Classes
data.classes.value_counts()
data.classes = data.classes.astype('category')
data["classes_cat"] = data.classes.cat.codes

data = data.drop(["buying","maint","doors","persons","lug_boot","safety","classes"],axis = 1)

X = data.drop(["classes_cat"],axis = 1).values
y = data["classes_cat"].values.flatten()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state = 1)

clf = tree.DecisionTreeClassifier()

clf.fit(X_train, y_train)

#max_leaf_nodes = 33,min_samples_split=4,min_samples_leaf=4,min_impurity_decrease=0.5

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy for Car Data: {}".format(accuracy))
#tree.plot_tree(clf.fit(X, y))

dot_data = tree.export_graphviz(clf, out_file=None, 
                     feature_names=["buying","maint","doors","persons","lug_boot","safety"],  
                     class_names=["unacc","acc","good","vgood"],  
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  
graph.render("car1") 