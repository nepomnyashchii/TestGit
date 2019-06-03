import mysql.connector
import requests
import json

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
    sql = " SELECT * FROM `todo`"
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
    sql = "DELETE FROM todo where id=" + str(id)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor)
    return mycursor.rowcount


def update_todo_by_id(id, text, done):
    myresult = ""
    mycursor = mydb.cursor()
    sql = "UPDATE todo SET `text` = '" + text + "', `done` = " + str(done) + "  WHERE id=" + str(id)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    return myresult
