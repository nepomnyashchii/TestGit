import mysql.connector
import requests
import json
def get_todo(id):
    myresult = ''
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="coolspammail",
        passwd="coolspammail-pass",
        database="coolspammail"
    )
    mycursor = mydb.cursor()
    # sql = "SELECT * FROM todo WHERE id = " + str(id) + ";"
    # mycursor.execute(sql)

    sql = "SELECT * FROM todo WHERE id = %s;"
    val = (id,)
    # necessary to put commar for the tuple at the end of the sentence
    mycursor.execute(sql, val)

    myresult = mycursor.fetchone()
    return myresult