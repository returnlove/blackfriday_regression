import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder


# https://github.com/justmarkham/DAT4/blob/master/notebooks/08_linear_regression.ipynb

def main():
	

	# read the data
	data_path = "../data/"
	train_file = data_path + "train.csv"
	test_file = data_path + "test.csv"
	train_data = pd.read_csv(train_file)
	test_data = pd.read_csv(test_file)

	print(train_data.shape)
	print(test_data.shape)
	print(train_data.info())
	print(train_data.head())

	# generate dummy variables using pandas
	for col in train_data.columns.values:
		print(train_data[col].dtype)
		if(train_data[col].dtype == 'object'):
			df = pd.get_dummies(train_data[col], prefix = col, sparse=True).astype(np.int8)
			print('df is')
			print(df)
			# print(col_dummies)


if __name__ == "__main__":
	main()