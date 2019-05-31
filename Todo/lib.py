import mysql.connector
import requests
import json

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

def insert_todo(text):
    # return_value = ""

    mydb = mysql.connector.connect(
        host="db4free.net",
        user="coolspammail",
        passwd="coolspammail-pass",
        database="coolspammail"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO todo (text, done) VALUES ( %s, "0")
    # necessary to put commar for the tuple at the end of the sentence
    val = (text, done)
    mycursor.execute(sql, val)

    print("1 record inserted, ID:", mycursor)
    return 1


