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
print("Using GaussianNB-",percent_same,'%')

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
print("HardCoded classifier-",percent_same1,'%')