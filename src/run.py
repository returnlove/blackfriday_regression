import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

def main():
	
	le = LabelEncoder()
	enc = OneHotEncoder()

	# read the data
	data_path = "../data/"
	train_file = data_path + "train.csv"
	test_file = data_path + "test.csv"
	train_data = pd.read_csv(train_file)
	test_data = pd.read_csv(test_file)

	print(train_data.shape)
	print(test_data.shape)
	print(train_data.info())
	print(train_data['Product_ID'].head())

	# if column is object then apply le
	for col in train_data.columns.values:
		if(train_data[col].dtypes == 'object'):
			data = train_data[col].append(test_data[col])
			# print('x train + test len: ' + str(len(data)))
			# print(len(data) == train_data.shape[0] + test_data.shape[0])
			# le fit should happen on whole data and transform the train and test data separately
			le.fit(data.values)
			train_data[col] = le.transform(train_data[col])
			test_data[col] = le.transform(test_data[col])

	print('label encoding, ok')
	print(train_data.shape)
	print(test_data.shape)
	print(train_data.info())
	print(train_data['Product_ID'].head())

	'''
	categorical_cols = 	["Gender","Age", "City_Category", "Stay_In_Current_City_Years"]

	for col in categorical_cols:
		data = train_data[col].append(test_data[col])
		# print('before enc')
		# print(data[col].value_counts.index)
		enc.fit(data)
		# print('after enc')
		# print(data[col].value_counts.index) # check before fit and after fit
		temp = enc.transform(train_data[col])
		temp = pd.DataFrame(temp, columns = [col+"_"+str(i) for i in data[col].value_counts.index])
		print('index values' + train_data.index.values)
		temp = temp.set_index(train_data.index.values)
		'''

if __name__ == "__main__":
	main()