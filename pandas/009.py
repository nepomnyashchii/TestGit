import pandas as pd

df = pd.read_csv('zillow.csv', index_col=0)
data= df.isnull()
data1=df.isnull().sum()
print(data)
print(data1)
