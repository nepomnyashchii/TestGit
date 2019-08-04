import pandas as pd
import mysql.connector

# """INSERT INTO xxx (OrderDate,Region,Rep,Item,Units,Unit Cost,Total)
#            VALUES ('%s', '%s', '%s', '%s', %s, %s, %s);"""

data = pd.read_excel('./data.xlsx', sheet_name='SalesOrders')


# options = make_options(parameter_sets_to_buffer=1000)

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail")

# conn = connect(driver='{SQL Server}', server='server_nm', database='db_nm', turbodbc_options=options)

test_query = ''' CREATE TABLE test_pandas2
                (OrderDate VARCHAR(255),
                    Region VARCHAR (255),
                    Rep VARCHAR (255),
                    Item VARCHAR (255),
                    Units INT,
                    Unit_Cost INT,
                    Total INT
                )

                INSERT INTO test_pandas (OrderData, Region, Rep, item, Units, Unit_Cost, Total)
                VALUES (%s,%s,%s,%s,%s,%s,%s)'''

mycursor = mydb.cursor()

mycursor.execute(test_query)
