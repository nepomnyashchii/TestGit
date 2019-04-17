import mysql.connector

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
    )
mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

