import pandas as pd
import mysql.connector


  """INSERT INTO xxx (OrderDate,Region,Rep,Item,Units,Unit Cost,Total)
         VALUES ('%s', '%s', '%s', '%s', %s, %s, %s);"""

data = pd.read_excel('./data.xlsx', sheet_name='SalesOrders')


# options = make_options(parameter_sets_to_buffer=1000)

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail")

# conn = connect(driver='{SQL Server}', server='server_nm', database='db_nm', turbodbc_options=options)

test_query = '''DROP TABLE IF EXISTS "test_pandas"

                CREATE TABLE Order
                (
                    OrderDate, VARCHAR(20)
                    Region,
                    Rep,
                    Item,
                    Units,
                    Unit Cost,
                    Total,
                )

                INSERT INTO test_pandas (OrderData, Region, Rep, item, Units, Unit Cost, Total)
                VALUES (%s,%s,%s,%s) '''

mycursor = mydb.cursor()

mycursor.executeman(test_query)

