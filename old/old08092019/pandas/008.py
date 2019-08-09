import pandas as pd


"""get_rid of indexes"""
df = pd.read_csv('zillow.csv', index_col=0)

"""drop columns"""

data= df.isnull()
data1=df.isnull().sum()
data2 = df.dropna()
"""drop rows"""
df.dropna(axis=1)
# print(data)
# print(data1)
df.shape
print(df.shape)
# print(data2)
