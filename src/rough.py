import pandas as pd


df = pd.DataFrame([['Sainath', 27],['test name', 20]], columns = ['name', 'age'])
# print(df)

df1 = pd.DataFrame([['hello', 1]], columns = ['name', 'age'])
# print(df1)

data = df.append(df1)
# print(data)

print('axis = 0')
data1 = pd.concat([df, df1], axis = 0)
print(data1)
print('      ')
print('axis = 1')
data2 = pd.concat([df, df1], axis = 1)
print(data2)