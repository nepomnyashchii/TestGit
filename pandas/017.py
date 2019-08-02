import pandas as pd

df = pd.read_csv('zillow.csv', index_col=0, skipinitialspace=True)
# print(type(df))

"""to read the data for the columns we need to skip initialspace"""

"""This way is to get a number"""


data = df[(df['Beds'] == 3) | (df['Baths'] == 4)].head()
print(data)