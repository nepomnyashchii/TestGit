import pandas as pd
import mysql.connector
from sqlalchemy.engine import create_engine

df = pd.read_excel('./data.xlsx', sheet_name='SalesOrders')
df=df.rename(columns={'Unit Cost' : 'Unit_Cost'})


print(df)

engine = create_engine(
    'mysql+mysqlconnector://coolspammail:coolspammail-pass@db4free.net/coolspammail')


data = df.to_sql(name = 'test_pandas2', con= engine, index=False, if_exists = "append")

