import mysql.connector

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
    )
mycursor = mydb.cursor()
mycursor.execute("SELECT name FROM customers")

myresult = mycursor.fetchall()

for row in myresult:
  print(row)