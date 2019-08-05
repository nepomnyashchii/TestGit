import sys
import pandas as pd

data = pd.read_excel('./data.xlsx', sheet_name='SalesOrders')
data2 = data.drop(columns=["OrderDate"])
print(data2)
data3 = data2.to_csv(index=False)
# print(data)
print(data3)
