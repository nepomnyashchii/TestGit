import mysql.connector
import pandas as pd
import openpyxl

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail")

sql = "SELECT * FROM secret"

mycursor = mydb.cursor()

mycursor.execute(sql)

myresult = mycursor.fetchall()

df = pd.DataFrame(myresult)

df.columns = mycursor.column_names

data = df.columns

data3 = df.to_csv(index=False)
data4 = df.to_excel(r'File Name.xlsx', index=False)

print(df)
print(data3)
# print(data4)


# mycursor.execute('SELECT * FROM table_name')

# table_rows = db_cursor.fetchall()

# df = pd.DataFrame(table_rows)

# sql = "SELECT msg, created, exp FROM secret WHERE id =  %s AND pin = %s"
# params = (sid, int(pin))
# mycursor.execute(sql, params)
# myresult = mycursor.fetchone()
# close_db(mydb)
# return_value = myresult
# logger.debug("Value from DB returned" + str(return_value))
