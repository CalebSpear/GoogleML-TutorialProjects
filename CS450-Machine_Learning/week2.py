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

#print(iris.data)
#print(iris.target)
#print(iris.target_names)

dtrain, dtest, ttrain, ttest = train_test_split(iris.data, iris.target, test_size = 0.3)

classifier = GaussianNB()
classifier.fit(dtrain, ttrain)
targets_predicted = classifier.predict(dtest)
equal = 0
j = 0
for i in ttest:
    #print(equal,ttest[j],targets_predicted[j])
    if ttest[j] == targets_predicted[j]:
        equal += 1
    j += 1
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
j = 0
for i in ttest:
    #print(i)
    if ttest[j] == targets_predicted1[j]:
        equal1 += 1
    j += 1
percent_same1 = equal1/len(ttest) * 100
#print("HardCoded classifier-",percent_same1,'%')

g = 0
same = 0
k = 3

def kNearest(k,indices):
        nearest = []
        for j in range(k):
            nearest.append(indices[j])
        return(nearest)

def distance(x,y):
    return np.sqrt(np.sum((x - y)**2))

for b in dtest:
    distances = []
    
    for i in dtrain:
        distances.append(distance(dtest[g],i))
    #print(distances)
        
    indices = np.argsort(distances)
    #print(indices)
    
    index = kNearest(k,indices)
    #print(index)
    
    m = 0
    target = []
    for n in index:
        target.append(ttrain[index[m]])
        m += 1
    #print(target)
    #print(iris.target_names)
    
    names = []
    w = 0
    for p in index:
        names.append(iris.target_names[target[w]])
        w += 1
    #print(iris.target_names)
    #print(stat.mode(names))
    
    #print(ttest[g],stat.mode(target))
    if ttest[g] == stat.mode(target):
        same += 1
    
    g += 1
    
percent_same2 = same/len(ttest) * 100
print('k-Nearest Neighbor Accuracy-',percent_same2,'%')

classifier2 = KNeighborsClassifier(n_neighbors=3)
classifier2.fit(dtrain, ttrain)
predictions = classifier2.predict(dtest)
s = 0
b = 0
for r in predictions:
    #print(ttest[b],predictions[b])
    if ttest[b] == predictions[b]:
        s += 1
    b += 1
#print(names)
ans = s/len(ttest) * 100
    
print('Existing Implementation-',ans,'%')