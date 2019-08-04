import pandas as pd
import mysql.connector
from sqlalchemy.engine import create_engine

df = pd.read_excel('./alec.xlsx')

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail")

engine = create_engine ('mysql+mysqlconnector://[coolspammail]:[coolspammail-pass]@[db4free.net]:[port]/[schema]')

connection = engine.connect()


data= df.to_sql('connection','test_pandas4', index =False)

test_query = '''INSERT INTO test_pandas4 (A,B) VALUES (%s, %s)'''

connection.execute(test_query, data)
