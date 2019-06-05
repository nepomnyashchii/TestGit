import mysql.connector


mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
)


def get_all():
    """get flowdata from db."""
    myresult = ''
    mycursor = mydb.cursor()
    sql = "SELECT * FROM `todo`"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult


def get_todo_by_id(id):
    myresult = ''
    mycursor = mydb.cursor()
    sql = "SELECT * FROM todo WHERE id = %s;"
    val = (id,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    return myresult


def insert_todo(text):
    mycursor = mydb.cursor()
    sql = "INSERT INTO `todo` (`text`,`done`) VALUES (%s,%s)"
    val = (text, 0)
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.lastrowid


def delete_todo_by_id(id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM todo where id=%s"
    val = (id,)
    mycursor.execute(sql,val)
    mydb.commit()
    return mycursor.rowcount


def update_todo_by_id(id, text, done):
    mycursor = mydb.cursor()
    sql = "UPDATE todo SET `text` = %s, `done` = %s  WHERE id=%s"
    val = (text, done, id)
    mycursor.execute(sql, val)
    mydb.commit()
    # print(mycursor.rowcount, "record(s) affected")
    return id
