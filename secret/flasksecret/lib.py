import uuid
import mysql.connector
import datetime
import time
import logger_module

logger = logger_module.setup_logger("secret-2lib")

def open_db():
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="coolspammail",
        passwd="coolspammail-pass",
        database="coolspammail"
    )
    return mydb

def is_not_expired(created, exp):
    try:
        my_time = created + datetime.timedelta(0, exp)
        current_time = datetime.datetime.utcnow()
        if my_time > current_time:
            return True
        else:
            return False
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

def put_secret(msg, pin, exp):
    """put secret into db table."""
    try:
        logger.debug("Invoke put_secret")
        sid = str(uuid.uuid4())
        logger.debug("sid " + str(sid))
        created = time.strftime('%Y-%m-%d %H:%M:%S')
        logger.debug("time created " + created)
        return_value = ''
        logger.debug('Invoke def open_db()')
        mydb = open_db()
        logger.debug("Start db")
        mycursor = mydb.cursor()
        sql = "INSERT INTO secret (id, msg, pin, exp, created) VALUES (%s, %s, %s, %s, %s)"
        val = (sid, msg, pin, exp, created)
        mycursor.execute(sql, val)
        logger.debug("Commit changes to the database")
        mydb.commit()
        logger.debug("Close the database")
        mydb.close()
        return_value = sid
        logger.debug("sid added to the database " + str(sid))
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


def get_secret(sid, pin):
    """get secret from db."""
    try:
        logger.debug("sid, pin " +str(sid) + " " + str(pin))
        print(sid, pin)
        print("Please wait...")
        return_value = ''
        logger.debug('Invoke def open_db()')
        mydb = open_db()
        logger.debug("Start db")
        mycursor = mydb.cursor()
        sql = "SELECT msg, created, exp FROM secret WHERE id =  %s AND pin = %s"
        params = (sid, int(pin))
        mycursor.execute(sql, params)
        myresult = mycursor.fetchone()
        logger.debug("Raw data from db " + " " + str(myresult))
        msg = myresult[0]
        logger.debug("Message " + msg)
        dbtime = myresult[1]
        logger.debug("Start dbtime " + str(dbtime))
        exp = myresult[2]
        logger.debug("Expiration time " + str(exp))

        if is_not_expired(dbtime, exp):
            return_value = msg
            logger.debug("Return message " +msg)
        else:
            return_value = "No such data"
        logger.debug("Close the database")
        mydb.close()

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


