from sklearn import datasets
from sklearn.linear_model import LinearRegression
import numpy as np

diabetes = datasets.load_diabetes()
# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

lm = LinearRegression()
lm.fit(diabetes_X_train, diabetes_y_train)
print(lm.score(diabetes_X_train, diabetes_y_train))
print(lm.score(diabetes_X_test, diabetes_y_test))
