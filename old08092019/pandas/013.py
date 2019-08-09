import pandas as pd

df = pd.read_csv('zillow.csv', index_col=0, skipinitialspace=True)
# print(type(df))

"""to read the data for the columns we need to skip initialspace"""

data = df.loc[10]

print(data)
