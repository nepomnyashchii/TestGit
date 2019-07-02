import mysql.connector


mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
)

def insert_todo(text):
    mycursor = mydb.cursor()
    sql = "INSERT INTO `todo` (`text`,`done`) VALUES (%s,%s)"
    val = (text, 0)
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.lastrowid

def update_todo_by_id(id, text, done):
    myresult = ""
    mycursor = mydb.cursor()
    sql = "UPDATE todo SET `text` = %s, `done` = %s  WHERE id=%s"
    val = (text, done, id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    return myresult
