import mysql.connector

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
    )
mycursor = mydb.cursor()

sql = "INSERT INTO products (name) VALUES"
val = [("Chocolate Heaven"),
("Tasty Lemons"),
("Vanilla Dreams")]


mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
