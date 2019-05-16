import uuid
import mysql.connector
import datetime
import time
import logging

logger = logging.getLogger('spam_application.lib')


def is_not_expired(created, exp):
    logger.debug('LIB: is_not_expired invoked')
    my_time = created + datetime.timedelta(0, exp)
    current_time = datetime.datetime.utcnow()
    # datetime.datetime.now()
    print(created, current_time, my_time)
    if my_time > current_time:
        logger.debug('is_not_expired return True')
        return True
    else:
        logger.debug('is_not_expired return False')
        return False


def put_secret(msg, pin, exp):
    """put secret into db table."""

    sid = str(uuid.uuid4())
    created = time.strftime('%Y-%m-%d %H:%M:%S')
    return_value = ''
    try:
        mydb = mysql.connector.connect(
            host="db4free.net",
            user="coolspammail",
            passwd="coolspammail-pass",
            database="coolspammail"
        )

        mycursor = mydb.cursor()
        sql = "INSERT INTO secret (id, msg, pin, exp, created) VALUES (%s, %s, %s, %s, %s)"
        val = (sid, msg, pin, exp, created)
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

        sql = "SELECT msg, created, exp FROM secret WHERE id =  %s AND pin = %s"
        params = (sid, int(pin))
        mycursor.execute(sql, params)
        myresult = mycursor.fetchone()
        msg = myresult[0]
        dbtime = myresult[1]
        exp = myresult[2]

        if is_not_expired(dbtime, exp):
            return_value = msg

    except:
        print("Record not found")

    # print(return_value)

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


def setup_logger():
    logger = logging.getLogger('spam_application')
    logger.setLevel(logging.DEBUG)

    dh = logging.FileHandler('debug.log')
    dh.setLevel(logging.DEBUG)

    eh = logging.FileHandler('error.log')
    eh.setLevel(logging.ERROR)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    dh.setFormatter(formatter)
    eh.setFormatter(formatter)

    logger.addHandler(eh)
    logger.addHandler(dh)
    return logger
