import mysql.connector

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
    )
mycursor = mydb.cursor()

sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
val = [('John', 154),
('Peter', 154),
('Amy', 155),
('Hannah', 20),
('Michael', 23)]


mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")