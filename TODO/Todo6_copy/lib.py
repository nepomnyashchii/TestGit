import mysql.connector
import logger_module
logger = logger_module.setup_logger("todo-2lib")
import json

def db_open():
    try:
        mydb = mysql.connector.connect(
            host="db4free.net",
            user="coolspammail",
            passwd="coolspammail-pass",
            database="coolspammail")
        return mydb
    except: "There is no connection"

def db_close():
    try:
        mydb_cl = mydb.close()
        return mydb_cl
    except: "Connection is broken"

def get_all():
    """get flowdata from db."""
    try:
        mydb
        mycursor = mydb.cursor()
        sql = "SELECT * FROM `todo`"
        mycursor.execute(sql)
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        rv = mycursor.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)

    except: print("Something went wrong in get_all")
    return json_data
mydb_cl



def get_todo_by_id(id):
    # myresult = ''
    try:
        mydb
        mycursor = mydb.cursor()
        sql = "SELECT * FROM todo WHERE id = %s;"
        val = (id,)
        mycursor.execute(sql, val)
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        rv = mycursor.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
            return json.dumps(json_data)
    except: print("Something went wrong with get_to_do_by_id")
    if "done" == 0 or "done"==1:
        return json_data
    else:return ("No real data exists")
    mydb_cl


def insert_todo(text):
    try:
        mydb
        mycursor = mydb.cursor()
        sql = "INSERT INTO `todo` (`text`,`done`) VALUES (%s,%s)"
        val = (text, 0)
        mycursor.execute(sql, val)
        mydb.commit()
        return mycursor.lastrowid
    except: print("Something went wrong with insert_todo")
    mydb_cl



def delete_todo_by_id(id):
    try:
        mydb
        mycursor = mydb.cursor()
        sql = "DELETE FROM todo where id=%s"
        val = (id,)
        mycursor.execute(sql,val)
        mydb.commit()
        return mycursor.rowcount
    except:print("Something went wrong with delete_todo_by_id")
    mydb_cl


def update_todo_by_id(id, text, done):
    try:
        mydb
        mycursor = mydb.cursor()
        sql = "UPDATE todo SET `text` = %s, `done` = %s  WHERE id=%s"
        val = (text, done, id)
        mycursor.execute(sql, val)
        mydb.commit()
        # print(mycursor.rowcount, "record(s) affected")
        return id
    except:  print("Something went wrong with updata_todo_by_id")
    mydb_cl

