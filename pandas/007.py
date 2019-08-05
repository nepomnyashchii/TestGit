import pandas as pd

df = pd.read_csv('zillow.csv', index_col=0)

df.columns = [col.lower() for col in df]

print(type(df.columns))


print(df.columns)
# print(df.rename)
