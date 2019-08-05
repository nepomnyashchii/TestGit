import pandas as pd

df = pd.read_csv('zillow.csv', index_col=0, skipinitialspace=True)

data =df
print(data)
print(type(df))
df.head()
data = df.tail(2)
# df.info()
df.shape
# print(df)

data=df.describe()
data1 = df.corr()
# print(df.columns)
# print(df.dtypes)
# print(df.values)
# print(data)
data = df*2
print(data)

""" Series is a single column of DataFrame"""



