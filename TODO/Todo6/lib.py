import json
import mysql.connector
import logger_module
logger = logger_module.setup_logger("todo-2lib")


def open_db():
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="coolspammail",
        passwd="coolspammail-pass",
        database="coolspammail"
    )
    return mydb


def close_db(mydb):
    mydb.close()


def get_all():
    """get flowdata from db."""

    try:
        mydb = open_db()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM `todo`"
        mycursor.execute(sql)
        # this will extract row headers
        row_headers = [x[0] for x in mycursor.description]
        rv = mycursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        close_db(mydb)
        return json.dumps(json_data)

    except:
        print("Something went wrong in get_all")
    return json_data


def get_todo_by_id(id):
    # myresult = ''
    try:
        mydb = open_db()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM todo WHERE id = %s;"
        val = (id,)
        mycursor.execute(sql, val)
        # this will extract row headers
        row_headers = [x[0] for x in mycursor.description]
        rv = mycursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        close_db(mydb)
    except:
        print("Something went wrong with get_to_do_by_id")
    if "done" == 0 or "done" == 1:
        return json.dumps(json_data)
        return json_data
    else:
        return ("No real data exists")


def insert_todo(text):
    try:
        mydb = open_db()
        mycursor = mydb.cursor()
        sql = "INSERT INTO `todo` (`text`,`done`) VALUES (%s,%s)"
        val = (text, 0)
        mycursor.execute(sql, val)
        mydb.commit()
        close_db(mydb)
        return mycursor.lastrowid
    except:
        print("Something went wrong with insert_todo")


def delete_todo_by_id(id):
    try:
        mydb = open_db()
        mycursor = mydb.cursor()
        sql = "DELETE FROM todo where id=%s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
        close_db(mydb)
        return mycursor.rowcount
    except:
        print("Something went wrong with delete_todo_by_id")


def update_todo_by_id(id, text, done):
    try:
        mydb = open_db()
        mycursor = mydb.cursor()
        sql = "UPDATE todo SET `text` = %s, `done` = %s  WHERE id=%s"
        val = (text, done, id)
        mycursor.execute(sql, val)
        mydb.commit()
        close_db(mydb)
        # print(mycursor.rowcount, "record(s) affected")
        return id
    except:
        print("Something went wrong with updata_todo_by_id")
