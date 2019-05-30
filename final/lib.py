import uuid
import mysql.connector
import logging
import logger_module

logger = logger_module.getModuleLogger('flowsapp.MYLIB')

def put_secret(msg, pin, exp):
    """put secret into db table."""
    sid = str(uuid.uuid4())
    return_value = ''
    try:
        mydb = mysql.connector.connect(
            host="db4free.net",
            user="coolspammail",
            passwd="coolspammail-pass",
            database="coolspammail"
        )

        mycursor = mydb.cursor()
        sql = "INSERT INTO secret (id, msg, pin, exp) VALUES (%s, %s, %s, %s)"
        val = (sid, msg, pin, exp)
        mycursor.execute(sql, val)
        mydb.commit()
        print("1 record inserted, ID:", mycursor)
        return_value = sid

    except:
        print("Something went wrong")

    return return_value


def get_secret(sid, pin):
    """get secret from db."""
    print(sid, pin)

    print("Please wait...")
    return_value = ''
    try:
        mydb = mysql.connector.connect(
            host="db4free.net",
            user="coolspammail",
            passwd="coolspammail-pass",
            database="coolspammail"
        )
        mycursor = mydb.cursor()

        sql = "SELECT msg FROM secret WHERE id =  %s AND pin = %s"
        params = (sid, int(pin))
        mycursor.execute(sql, params)
        myresult = mycursor.fetchone()
        return_value = myresult[0]
    except:
        print("Record not found")

    return return_value


def del_secret(sid, pin):
    """del secret from db."""
    print(sid, pin)

    print("Please wait...")
    return_value = ''
    try:
        mydb = mysql.connector.connect(
            host="db4free.net",
            user="coolspammail",
            passwd="coolspammail-pass",
            database="coolspammail"
        )
        mycursor = mydb.cursor()

        # DELETE FROM secret WHERE id = '5d025a4c-5991-457d-a8f9-3e27de288b19' AND pin = 1234

        sql = "DELETE FROM secret WHERE id =  %s AND pin = %s"
        params = (sid, int(pin))
        mycursor.execute(sql, params)
        myresult = mycursor.fetchone()
        print(myresult)
        return_value = myresult[0]
    except:
        print("Record not found")

    return return_value
