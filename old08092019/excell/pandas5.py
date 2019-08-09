import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail")

sql = "SELECT * FROM test_pandas2"

mycursor = mydb.cursor()

mycursor.execute(sql)

myresult = mycursor.fetchall()

df = pd.DataFrame(myresult)

df.columns = mycursor.column_names

data = df.columns

data2 = df.to_excel(r'new_data.xlsx', index=False)

print(df)

# print(data3)