import mysql.connector

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")