import pandas as pd

df = pd.read_csv('zillow.csv', index_col=0)
print(type(df))
df.head()
data = df.tail(2)
# df.info()
df.shape
# print(df)

data=df.describe()
data1 = df.corr()
# s = df['Baths']
# # genre_col = df['Baths']
# print(data)
# print(s)
# print(genre_col)
# print(type(genre_col))
