import mysql.connector

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
    )
mycursor = mydb.cursor()

sql = "INSERT INTO products (name) VALUES (%s)"
val = [("Cake",),
("Telephone",),
("Music",)]


mycursor.executemany(sql, val)

mydb.commit()

print(mycursor)