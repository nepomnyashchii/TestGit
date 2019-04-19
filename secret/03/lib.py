import uuid
import mysql.connector


def put_secret(msg, pin, exp):
    """put secret into db table."""
    sid = str(uuid.uuid4())
    print(msg, exp, pin, sid)
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
        sql = "INSERT INTO secret (id, msg, pin, exp) VALUES (%s, %s, %s, %s)"
        val = (sid, msg, pin, exp)
        mycursor.execute(sql, val)
        mydb.commit()
        print("1 record inserted, ID:", mycursor.lastrowid)
        return_value = sid

    except:
        print("Something went wrong")

    return return_value


def get_secret(sid, pin):
    """get secret from db."""
    print(sid, pin)
    return "ura"
