import mysql.connector

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
    )

mycursor = mydb.cursor()

x= mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
print(x)
