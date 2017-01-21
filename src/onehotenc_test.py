from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def get_expanded_col_names(cols, sub_cols):
    res = []
    if len(cols) != len(sub_cols):
        raise "cols and expanded sub columns are not consistent"
    for i in range(len(cols)):
        prefix = cols[i]
        sub_num = sub_cols[i]
        for j in range(sub_num):
            res.append(prefix + '_' + str(j + 1))
    return res


enc = OneHotEncoder(sparse=True)
df = pd.DataFrame([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]], columns=['a', 'b','c'])
print(df)
enc.fit(df)
print('fit ok')

df_test = pd.DataFrame([[0, 1, 1], [1, 1, 2]], columns=['a', 'b','c'])
print('new df')
print(df_test)

arr = enc.transform(df_test)
print(arr)
print('transform ok')


columns = get_expanded_col_names(df_test.columns, enc.n_values_)
df_res = pd.DataFrame(arr, columns=columns)
print df_res
