from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier

data = np.random.normal(1,4,1000)
data = np.append(data,np.random.normal(5,4,1000))

data0 = data[0:1000]
data1 = data[1000:2000]

target = np.zeros(1000)
target = np.append(target,np.full(1000,1))

X_train, X_test, y_train, y_test = train_test_split(data.reshape(-1,1), target, test_size=0.2)

classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Gaussian Naive Bayes Accuracy: {}".format(accuracy))

classifier1 = KNeighborsClassifier(n_neighbors=5)
classifier1.fit(X_train, y_train)

y_pred1 = classifier1.predict(X_test)

accuracy = accuracy_score(y_test, y_pred1)
print("Nearest Neighbor Accuracy: {}".format(accuracy))

classifier2 = SVC(kernel='linear')
classifier2.fit(X_train, y_train)

y_pred2 = classifier2.predict(X_test)

accuracy = accuracy_score(y_test, y_pred2)
print("Support Vector Machine Accuracy: {}".format(accuracy))

classifier3 = DecisionTreeClassifier()
classifier3.fit(X_train, y_train)

y_pred3 = classifier3.predict(X_test)

accuracy = accuracy_score(y_test, y_pred3)
print("Decision Tree Accuracy: {}".format(accuracy))

#print(confusion_matrix(y_test,y_pred))
#print(classification_report(y_test,y_pred))