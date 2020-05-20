import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

os.chdir("/Users/caleb/Downloads")

names = ["mpg","cylinders","displacement","horsepower","weight","acceleration",
         "model_year","origin","car_name"]
         
data = pd.read_csv("autompg.data", header=None, delimiter= '\s+', skipinitialspace=True,
                   names=names, na_values=["?"])

add = 0
length = 0
for i in range(len(data.horsepower)):
    if not data.isnull().horsepower[i]:
        add += data.horsepower[i]
        length += 1
    
data.horsepower = data.horsepower.fillna(int(add/length))

data[data.isnull().any(axis=1)]
#print(data.isnull().any())

# Car Name- Label
#data.car_name.value_counts()
#data.car_name = data.car_name.astype('category')
#data["car_name_cat"] = data.car_name.cat.codes
#print(data.car_name_cat)
    
std_scale = StandardScaler().fit(data[['cylinders','displacement', 'horsepower', 'weight', 'acceleration',"model_year","origin"]])
data_std = std_scale.transform(data[['cylinders','displacement', 'horsepower', 'weight', 'acceleration',"model_year","origin"]])
data.cylinders = data_std[:,0]
data.displacement = data_std[:,1]
data.horsepower = data_std[:,2]
data.weight = data_std[:,3]
data.acceleration = data_std[:,4]
data.model_year = data_std[:,5]
data.origin = data_std[:,6]

# Car Name- One Hot
data.car_name.value_counts()
data = pd.get_dummies(data, columns=["car_name"])

X = data.drop(["mpg"],axis = 1).as_matrix()
y = data["mpg"].as_matrix().flatten()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

regr = KNeighborsRegressor(n_neighbors=5)

regr.fit(X_train, y_train)

y_pred = regr.predict(X_test)

per_error = (abs(y_test - y_pred))/y_test
mean_per_error = np.mean(per_error)
print("MPG Mean Percent Error: {}".format(mean_per_error))

error = mean_squared_error(y_test, y_pred)
#print(y_pred,"\n",y_test)
print("MPG Mean Squared Error: {}".format(error))