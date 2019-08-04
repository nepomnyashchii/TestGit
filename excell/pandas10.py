import pandas as pd
import mysql.connector
from sqlalchemy.engine import create_engine

df = pd.read_excel('./alec.xlsx')

engine = create_engine(
    'mysql+mysqlconnector://coolspammail:coolspammail-pass@db4free.net/coolspammail')


data = df.to_sql(name = 'test_pandas', con='connection', index=False, if_exists = "append")

