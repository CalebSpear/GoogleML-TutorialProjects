import os
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

os.chdir("/Users/caleb/Downloads")
         
data = pd.read_csv("student-mat.csv", sep=';',skipinitialspace=True, na_values=["?"])

#print(data)

data[data.isnull().any(axis=1)]
#print(data.isnull().any())

# School
data.school.value_counts()
data["isGP"] = data.school.map({"GP": 1, "MS": 0})

# Sex
data.sex.value_counts()
data["isMale"] = data.sex.map({"M": 1, "F": 0})

# Address
data.address.value_counts()
data["isUrban"] = data.address.map({"U": 1, "R": 0})

# Family Size
data.famsize.value_counts()
data["isSmall"] = data.famsize.map({"LE3": 1, "GT3": 0})

# Parental Status
data.Pstatus.value_counts()
data["isTogether"] = data.Pstatus.map({"T": 1, "A": 0})

#Mother's Job
data.Mjob.value_counts()
data = pd.get_dummies(data, columns=["Mjob"])

#Father's Job
data.Fjob.value_counts()
data = pd.get_dummies(data, columns=["Fjob"])

#Reason
data.reason.value_counts()
data = pd.get_dummies(data, columns=["reason"])

#Guardian
data.guardian.value_counts()
data = pd.get_dummies(data, columns=["guardian"])

# School Support
data.schoolsup.value_counts()
data["isYesss"] = data.schoolsup.map({"yes": 1, "no": 0})

# Family Support
data.famsup.value_counts()
data["isYesfs"] = data.famsup.map({"yes": 1, "no": 0})

# Paid
data.paid.value_counts()
data["isYesp"] = data.paid.map({"yes": 1, "no": 0})

# Activities
data.activities.value_counts()
data["isYesa"] = data.activities.map({"yes": 1, "no": 0})

# Nursery
data.nursery.value_counts()
data["isYesn"] = data.nursery.map({"yes": 1, "no": 0})

# Higher
data.higher.value_counts()
data["isYesh"] = data.higher.map({"yes": 1, "no": 0})

# Internet
data.internet.value_counts()
data["isYesi"] = data.internet.map({"yes": 1, "no": 0})

# Romantic
data.romantic.value_counts()
data["isYesr"] = data.romantic.map({"yes": 1, "no": 0})

data = data.drop(["school","sex","address","famsize","Pstatus","schoolsup","famsup",
                  "paid","activities","nursery","higher","internet","romantic"],axis = 1)

X = data.drop(["G3"],axis = 1).values
y = data["G3"].values.flatten()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

regr = KNeighborsRegressor(n_neighbors=5)

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