import mysql.connector
import requests
import json

mydb = mysql.connector.connect(
        host="db4free.net",
        user="coolspammail",
        passwd="coolspammail-pass",
        database="coolspammail"
    )

# def get_todo():
#     """get flowdata from db."""
#     myresult = ''
#     mydb = mysql.connector.connect(
#             host="db4free.net",
#             user="coolspammail",
#             passwd="coolspammail-pass",
#             database="coolspammail"
#         )

#     mycursor = mydb.cursor()
#     sql = " SELECT * FROM `todo`"
#     mycursor.execute(sql)
#     myresult = mycursor.fetchall()
#     return myresult


# def get_todo(id):
#     myresult = ''
#     mydb = mysql.connector.connect(
#         host="db4free.net",
#         user="coolspammail",
#         passwd="coolspammail-pass",
#         database="coolspammail"
#     )
#     mycursor = mydb.cursor()
#     # sql = "SELECT * FROM todo WHERE id = " + str(id) + ";"
#     # mycursor.execute(sql)

#     sql = "SELECT * FROM todo WHERE id = %s;"
#     val = (id,)
#     # necessary to put commar for the tuple at the end of the sentence
#     mycursor.execute(sql, val)

#     myresult = mycursor.fetchone()
#     return myresult

# def insert_todo(text):
#     mycursor = mydb.cursor()
#     sql = "INSERT INTO `todo` (`text`,`done`) VALUES (%s,%s)"
#     val = (text, 0)
#     mycursor.execute(sql, val)
#     mydb.commit()
#     return mycursor.lastrowid

# def delete_todo():

#     mydb = mysql.connector.connect(
#     host="db4free.net",
#     user="coolspammail",
#     passwd="coolspammail-pass",
#     database="coolspammail"
#     )
#     mycursor = mydb.cursor()

#     sql = "DELETE FROM todo where id=2"

#     mycursor.execute(sql)

#     mydb.commit()

#     print(mycursor.rowcount, "record(s) deleted")

def update_todo ():
    myresult =" "
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="coolspammail",
        passwd="coolspammail-pass",
        database="coolspammail"
    )
    mycursor = mydb.cursor()

    sql = "UPDATE todo SET `text` = 'drink' WHERE id=3"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")
    return myresult







