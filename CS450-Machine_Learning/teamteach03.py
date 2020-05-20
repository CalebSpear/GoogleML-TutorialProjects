import os
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense


os.chdir("/Users/caleb/Downloads")

names = ["age", "workclass", "fnlwgt", "education", "education_num", "marital_status",
         "occupation", "relationship", "race", "sex", "capital_gain", "capital_loss",
         "hours_per_week", "native_country", "income"]
         
data = pd.read_csv("adultdata.txt", header=None, skipinitialspace=True,
                   names=names, na_values=["?"])

#print(data)
#print(data.columns)
#print(data.dtypes)

#print(data.age.median())
#print(data.native_country.value_counts())

data[data.isnull().any(axis=1)]
data.isnull().any()
data.workclass = data.workclass.fillna("unknown")
data.native_country = data.native_country.fillna("unknown")
data.occupation = data.occupation.fillna("unknown")
data[data.isnull().any(axis=1)]
data.isnull().any()

#print(data.select_dtypes(include=["object"]).columns)

# Workclass
data.workclass.value_counts()
data.workclass = data.workclass.astype('category')
data["workclass_cat"] = data.workclass.cat.codes

# education
data.education.value_counts()
data.education = data.education.astype('category')
data["education_cat"]= data.education.cat.codes

# marital_status
data.marital_status.value_counts()
data.marital_status = data.marital_status.astype('category')
data["marital_status_cat"]= data.marital_status.cat.codes

# occupation
data.occupation.value_counts()
data.occupation = data.occupation.astype('category')
data["occupation_cat"]= data.occupation.cat.codes

# relationship
data.relationship.value_counts()
data.relationship = data.relationship.astype('category')
data["relationship_cat"]= data.relationship.cat.codes

# race
data.race.value_counts()
data = pd.get_dummies(data, columns=["race"])

# sex
data.sex.value_counts()
data["isMale"] = data.sex.map({"Male": 1, "Female": 0})

# native_country
data.native_country.value_counts()
data.native_country = data.native_country.astype('category')
data["native_country_cat"]= data.native_country.cat.codes

# income (our target)
data.income.value_counts()
data["incomeHigh"] = data.income.map({">50K": 1, "<=50K": 0})

data = data.drop(["workclass", "education", "marital_status", "occupation",
                   "relationship", "sex", "native_country", "income"],axis = 1)
                   
# First convert the data to numpy arrays, because that's what sk-learn likes
X = data.drop(["incomeHigh"],axis = 1).values
y = data["incomeHigh"].values.flatten()

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu')) 
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, epochs=1, batch_size=10)

accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))