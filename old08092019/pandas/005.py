import pandas as pd

df = pd.read_csv('zillow.csv', index_col=0)
df.head()
data = df.tail(2)
# df.info()
df.shape
# print(df)

"""we can see five top rows of the data"""

# print(data)
# print(df.head())
# print(df.info())
print(df.shape)