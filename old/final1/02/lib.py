import datetime
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


def is_expired(created, exp):
    """get time if needed."""
    my_time = created + datetime.timedelta(0, exp)
    current_time = datetime.datetime.now()
    # print(created, current_time, my_time)
    if my_time > current_time:
        return True
    else:
        return False
