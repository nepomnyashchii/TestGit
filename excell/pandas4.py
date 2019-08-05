import pandas as pd
import mysql.connector
import sqlalchemy
from sqlalchemy.engine import create_engine


engine = create_engine(
    'mysql+mysqlconnector://coolspammail:coolspammail-pass@db4free.net/coolspammail')

print(type (engine))

sql = '''SELECT * FROM test_pandas2'''
df = pd.read_sql(sql, engine)

print(type(df))

data = df.to_excel('sqlalchemy.xlsx', index=False)

print(type(data))

# df = pd.read_sql_table("test_pandas_2", engine)


print(df)