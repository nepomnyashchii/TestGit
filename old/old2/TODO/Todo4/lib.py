import mysql.connector
import logger_module
logger = logger_module.setup_logger("todo-2lib")
import json



mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
)

def get_all():
    """get flowdata from db."""
    try:
        mycursor = mydb.cursor()
        sql = "SELECT * FROM `todo`"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
    except: print("Something went wrong in get_all")
    return json.dumps(myresult)



def get_todo_by_id(id):
    # myresult = ''
    try:
        mycursor = mydb.cursor()
        sql = "SELECT * FROM todo WHERE id = %s;"
        val = (id,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
    except: print("Something went wrong with get_to_do_by_id")
    return json.dumps(myresult)


def insert_todo(text):
    try:
        mycursor = mydb.cursor()
        sql = "INSERT INTO `todo` (`text`,`done`) VALUES (%s,%s)"
        val = (text, 0)
        mycursor.execute(sql, val)
        mydb.commit()
        return mycursor.lastrowid
    except: print("Something went wrong with insert_todo")



def delete_todo_by_id(id):
    try:
        mycursor = mydb.cursor()
        sql = "DELETE FROM todo where id=%s"
        val = (id,)
        mycursor.execute(sql,val)
        mydb.commit()
        return mycursor.rowcount
    except:print("Something went wrong with delete_todo_by_id")


def update_todo_by_id(id, text, done):
    try:
        mycursor = mydb.cursor()
        sql = "UPDATE todo SET `text` = %s, `done` = %s  WHERE id=%s"
        val = (text, done, id)
        mycursor.execute(sql, val)
        mydb.commit()
        # print(mycursor.rowcount, "record(s) affected")
        return id
    except:  print("Something went wrong with updata_todo_by_id")

