import pandas as pd

df = pd.read_csv('zillow.csv', index_col=0, skipinitialspace=True)
# print(type(df))

"""to read the data for the columns we need to skip initialspace"""
"""Rename the column name from Baths to Bathroom"""
data = df.rename(columns={
    "Baths": "Bathroom"})
# print(df.columns)
# movies_df.rename(columns={
#         'Runtime (Minutes)': 'Runtime',
#         'Revenue (Millions)': 'Revenue_millions'
#     }, inplace=True)

print (data)
