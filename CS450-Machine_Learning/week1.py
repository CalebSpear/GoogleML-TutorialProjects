# -*- coding: utf-8 -*-
"""
Caleb Spear
CS450
"""

from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import statistics as stat
iris = datasets.load_iris()

print(iris)
#print(iris.target)
print(iris.feature_names)

dtrain, dtest, ttrain, ttest = train_test_split(iris.data, iris.target, test_size = 0.3)

classifier = GaussianNB()
classifier.fit(dtrain, ttrain)
targets_predicted = classifier.predict(dtest)
equal = 0
for i in ttest:
    if ttest[i] == targets_predicted[i]:
        equal += 1
percent_same = equal/len(ttest) * 100
#print(ttest)
#print(targets_predicted)
#print(equal,len(ttest))
#print("Using GaussianNB-",percent_same,'%')

class HardCodedClassifier():
    def __init__(self):
        pass
    
    def fit(self,dtrain,ttrain):
        pass
        
    def predict(self,dtest):
        zeros = []
        for i in dtest:
            zeros.append(0)
        return zeros

classifier1 = HardCodedClassifier()
classifier1.fit(dtrain, ttrain)
targets_predicted1 = classifier1.predict(dtest)
equal1 = 0
for i in ttest:
    if ttest[i] == targets_predicted1[i]:
        equal1 += 1
percent_same1 = equal1/len(ttest) * 100
#print("HardCoded classifier-",percent_same1,'%')

x = [ 6,3,5.5,2]
def distance(x,y):
    return np.sqrt(np.sum((x - y)**2))

distances = []
for i in iris.data:
    distances.append(distance(x,i))
    
indices = np.argsort(distances)
k = 50
#print(indices)

def kNearest(k,indices):
    nearest = []
    for j in range(k):
        nearest.append(indices[j])
    return(nearest)
index = kNearest(k,indices)
#print(len(index))
m = 0
tar = []
for n in index:
    tar.append(iris.target[index[m]])
    m += 1
#print(tar)
#print(iris.target_names)
names = []
l = 0
for p in index:
    names.append(iris.target_names[tar[l]])
    l += 1
#print(names)
print(stat.mode(names))

classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(dtrain, ttrain)
predictions = classifier.predict(dtest)
names1 = []
s = 0
for r in predictions:
    names1.append(iris.target_names[predictions[s]])
    s += 1
#print(names)
print(stat.mode(names1))