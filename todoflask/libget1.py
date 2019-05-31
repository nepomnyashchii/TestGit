import mysql.connector
import requests
import json
def get_todo():
    """get flowdata from db."""
    myresult = ''
    mydb = mysql.connector.connect(
            host="db4free.net",
            user="coolspammail",
            passwd="coolspammail-pass",
            database="coolspammail"
        )

    mycursor = mydb.cursor()
    sql = " SELECT * FROM `todo`"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult
