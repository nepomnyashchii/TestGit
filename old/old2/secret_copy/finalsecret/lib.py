import uuid
import mysql.connector
import datetime
import time
import logging
import logger_module

logger = logger_module.getModuleLogger('flowsapp.MYLIB')

def is_not_expired(created, exp):
    my_time = created + datetime.timedelta(0, exp)
    current_time = datetime.datetime.utcnow()
    # datetime.datetime.now()
    print(created, current_time, my_time)
    if my_time > current_time:
        return True
    else:
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

    except IOError:
        logger.error('An error occured trying to read the file.')
    except ValueError:
        logger.error('Non-numeric data found in the file.')
    except ImportError:
        logger.error("NO module found")
    except EOFError:
        logger.error('Why did you do an EOF on me?')
    except KeyboardInterrupt:
        logger.error('You cancelled the operation.')
    except:
        logger.debug('An error occured.')

    return return_value



