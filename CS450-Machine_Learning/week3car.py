import os
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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

X = data.drop(["classes_cat"],axis = 1).as_matrix()
y = data["classes_cat"].as_matrix().flatten()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

classifier = KNeighborsClassifier(n_neighbors=5)

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy for Car Data: {}".format(accuracy))