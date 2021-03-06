import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder


# https://github.com/justmarkham/DAT4/blob/master/notebooks/08_linear_regression.ipynb

def to_dummy(col):
		var_name =  pd.get_dummies(train_data[col], prefix = col)
		return var_name

def main():
	

	# read the data
	data_path = "../data/"
	train_file = data_path + "train.csv"
	test_file = data_path + "test.csv"
	train_data = pd.read_csv(train_file)
	global train_data
	test_data = pd.read_csv(test_file)

	print(train_data.shape)
	print(test_data.shape)
	print(train_data.info())
	print(train_data.head())

	cat_columns = []

	# generate dummy variables using pandas
	for col in train_data.columns.values:
		print(train_data[col].dtype)
		if(train_data[col].dtype == 'object'):
			cat_columns.append(col)

	print(cat_columns)

	cat_columns.append('Occupation')
	cat_columns.append('Product_Category_1')
	print(cat_columns)
	cat_columns.remove('Product_ID')
	print(cat_columns)

	train_data_new = pd.DataFrame()

	for col in cat_columns:
		var = col+"_dummy"
		var = pd.get_dummies(train_data[col], prefix = col).iloc[:,1:]
		# print(var.head())
		train_data_new = pd.concat([train_data_new, var], axis = 1)
		# train_data_new.append()

	print('train data new ')
	print(train_data_new.info())
	# Gender_dummy = pd.get_dummies(train_data['Gender'], prefix = 'gender').iloc[:,1:]
	# print(Gender_dummy)

	# print(create_var_name('hello'))
	# print(to_dummy(cat_columns[2]))

	# check train columns names
	print('train_data####')
	print(train_data.info())

	new_cols = train_data_new.columns.values
	old_cols = train_data.columns.values

	print(new_cols)
	print(old_cols)	
	train_data_new = pd.concat([train_data_new, train_data['Marital_Status']], axis = 1)
	print(train_data_new.columns.values)

	x_train = train_data_new
	y_train = train_data['Purchase']

	model = LinearRegression()
	model.fit(x_train, y_train)
	print('R sqaured score is: ')

	print(model.score(x_train, y_train))


if __name__ == "__main__":
	main()
