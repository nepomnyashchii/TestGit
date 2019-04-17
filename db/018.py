import mysql.connector

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
    )
mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")



