import uuid
import mysql.connector


mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail")


def put_secret(msg, pin, exp):
    """put secret into db table."""
    sid = str(uuid.uuid4())
    print(msg, exp, pin, sid)
    return sid


def get_secret(sid, pin):
    """get secret from db."""
    print(sid, pin)
    return "ura"
