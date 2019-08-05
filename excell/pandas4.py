import pandas as pd
import mysql.connector
import sqlalchemy
from sqlalchemy.engine import create_engine


engine = create_engine(
    'mysql+mysqlconnector://coolspammail:coolspammail-pass@db4free.net/coolspammail')


df = pd.read_sql_table("test_pandas", engine)


# print(df)