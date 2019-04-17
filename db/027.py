import mysql.connector

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
    )
mycursor = mydb.cursor()

sql = "SELECT \
  customers.name AS customers, \
  customs.name AS address \
  FROM customers \
  INNER JOIN customs ON customers.address = customs.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)