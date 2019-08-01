import uuid
import mysql.connector
import datetime
import time
import logger_module
import config

logger = logger_module.setup_logger("dblib")


def open_db():
    try:
        logger.debug('open_db function invoked')
        mydb = mysql.connector.connect(
            host= dbconne
            user="coolspammail",
            passwd="coolspammail-pass",
            database="coolspammail"
        )
        logger.debug('open_db finished')
        return mydb
    except mysql.connector.Error as error:
        logger.error('There is no DB connection: {}'.format(error))


def close_db(mydb):
    try:
        logger.debug("close_db function invoked")
        mydb.close()
        logger.debug("close_db finished")

    except mysql.connector.Error:
        logger.error(
            'Something happened with the server: {}'.format(logger.error))


def is_not_expired(created, exp):
    try:
        logger.debug(
            "is_not expired function to control expiration time of the msg invoked")
        my_time = created + datetime.timedelta(0, exp)
        logger.debug("Time before expiration: " + str(my_time))
        current_time = datetime.datetime.utcnow()
        logger.debug("Current time: " + str(current_time))
        if my_time > current_time:
            logger.debug("is_not_expired: return True")
            return True
        else:
            logger.debug("is_not_expired: return False")
            return False

    except ValueError:
        logger.error('Non-numeric data found in the file.')
    except Exception as error:
        logger.error(error)


def put_secret(msg, pin, exp):
    """put secret into db table."""
    try:
        logger.debug("put_secret function invoked")
        sid = str(uuid.uuid4())
        logger.debug("sid: " + str(sid))
        created = time.strftime('%Y-%m-%d %H:%M:%S')
        logger.debug("Time created: " + str(created))
        return_value = ''
        mydb = open_db()
        if mydb is not None:
            mycursor = mydb.cursor()
            sql = "INSERT INTO secret (id, msg, pin, exp, created) VALUES (%s, %s, %s, %s, %s)"
            val = (sid, msg, pin, exp, created)
            mycursor.execute(sql, val)
            logger.debug("Commit changes to the database")
            mydb.commit()
            close_db(mydb)
            return_value = sid
            logger.debug("sid added to the database: " + str(sid))
    except mysql.connector.Error:
        logger.error('Something went wrong: {}'.format(logger.error))

    return return_value


def get_secret_from_db(sid, pin):
    """get secret from db."""
    try:
        logger.debug("get_secret _from_db function invoked, sid, pin: " + str(sid) + " " + str(pin))
        print("DB wait...")
        mydb = open_db()
        return_value = ""
        if mydb is not None:
            mycursor = mydb.cursor()
            sql = "SELECT msg, created, exp FROM secret WHERE id =  %s AND pin = %s"
            params = (sid, int(pin))
            mycursor.execute(sql, params)
            myresult = mycursor.fetchone()
            close_db(mydb)
            return_value = myresult
            logger.debug("Value from DB returned" + str(return_value))
    except mysql.connector.Error as error:
        logger.error(error)
    return return_value


def get_secret(sid, pin):
    try:
        logger.debug("get_secret function invoked")
        myresult = get_secret_from_db(sid, pin)
        if myresult is not None:
            logger.debug("Raw data from db: " + " " + str(myresult))
            msg = myresult[0]
            logger.debug("Message: " + msg)
            dbtime = myresult[1]
            logger.debug("Start dbtime: " + str(dbtime))
            exp = myresult[2]
            logger.debug("Expiration time in seconds: " + str(exp))
            if is_not_expired(dbtime, exp):
                return_value = msg
                logger.debug("Return message: " + msg)
            else:
                return_value = ""
        else:
            return_value = ""
        return return_value
    except ValueError:
        logger.error('Non-numeric data found in the file.')
    except Exception as error:
        logger.error(error)


def del_secret(sid, pin):
    """del secret from db."""
    try:
        logger.debug("del_secret function invoked")
        print("Please wait...")
        mydb = open_db()
        logger.debug("Start db")
        mycursor = mydb.cursor()
        sql = "DELETE FROM secret WHERE id =  %s AND pin = %s"
        params = (sid, int(pin))
        mycursor.execute(sql, params)
        mydb.commit()
        close_db(mydb)
        if mycursor.rowcount == 1:
            return True
        return False
    except mysql.connector.Error as error:
        logger.error(error)
