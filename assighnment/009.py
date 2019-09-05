import mysql.connector

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
)

mycursor = mydb.cursor()

y = mycursor.execute(
    "CREATE TABLE clients (name VARCHAR(255), phone VARCHAR(255), email VARCHAR(255))")
print(y)
