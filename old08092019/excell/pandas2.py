import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail")

test_query = ''' CREATE TABLE test_pandas3
                (OrderDate DATE PRIMARY KEY,
                    Region VARCHAR (255),
                    Rep VARCHAR (255),
                    Item VARCHAR (255),
                    Units INT,
                    Unit_Cost INT,
                    Total INT
                ) '''

mycursor = mydb.cursor()

mycursor.execute(test_query)
