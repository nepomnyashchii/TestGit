import pandas as pd
import mysql.connector
from sqlalchemy.engine import create_engine

df = pd.read_excel('./alec.xlsx')

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail")


c = mydb.cursor()

# data= df.to_sql(mydb,'test_pandas4', index =False)

test_query = ''' CREATE TABLE test_pandas
                (A INT,
                B VARCHAR (255)
                ) '''

c = mydb.cursor()

c.execute(test_query)
