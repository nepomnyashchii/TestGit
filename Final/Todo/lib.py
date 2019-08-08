import config
import json
import mysql.connector
import logger_module
logger = logger_module.setup_logger("todo-2lib")


def open_db():
    try:
        logger.debug('open_db function invoked')
        mydb = mysql.connector.connect(
            host=config.dbconnection["host"],
            user=config.dbconnection["user"],
            passwd=config.dbconnection["passwd"],
            database=config.dbconnection["database"]
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

def insert_username_todo(username):
    try:
        logger.debug('Invoke: def open_db()')
        mydb = open_db()
        logger.debug("Start db")
        mycursor = mydb.cursor()
        sql = "INSERT INTO `todo` (username) VALUES (%s)"
        val = (username,)
        mycursor.execute(sql, val)
        logger.debug("Commit changes to the database")
        mydb.commit()
        logger.debug("Invoke: def close_db(mydb)")
        close_db(mydb)
        return mycursor.lastrowid
    except Exception as error:
        logger.error(error)


def get_all():
    """get flowdata from db."""

    try:
        logger.debug('Invoke: def open_db()')
        mydb = open_db()
        logger.debug("Start db")
        mycursor = mydb.cursor()
        logger.debug("Start executing action for db")
        sql = "SELECT * FROM `todo`"
        mycursor.execute(sql)
        # this will extract row headers
        logger.debug("Collect list of tuples for all ids")
        rv = mycursor.fetchall()
        logger.debug("All obtained data from database" + str(rv))
        row_headers = [x[0] for x in mycursor.description]
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        logger.debug(
            "Create dictionary with inserted row_headers from tuple" + str(json_data))
        logger.debug("Invoke: def close_db(mydb)")
        close_db(mydb)
    except Exception as error:
        logger.error(error)
    return json_data


def get_todo_by_id(id):
    # myresult = ''
    try:
        logger.debug('Invoke: def open_db()')
        mydb = open_db()
        logger.debug("Start db")
        mycursor = mydb.cursor()
        sql = "SELECT * FROM todo WHERE id = %s;"
        val = (id,)
        mycursor.execute(sql, val)
        # this will extract row headers
        logger.debug("Collect list of tuples for all ids")
        rv = mycursor.fetchall()
        logger.debug("All obtained data from database" + str(rv))
        row_headers = [x[0] for x in mycursor.description]
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        logger.debug(
            "Create dictionary with inserted row_headers from tuples" + str(json_data))
        logger.debug("Invoke: def close_db(mydb)")
        close_db(mydb)
        return json_data
    except Exception as error:
        logger.error(error)


def insert_todo(text):
    try:
        logger.debug('Invoke: def open_db()')
        mydb = open_db()
        logger.debug("Start db")
        mycursor = mydb.cursor()
        sql = "INSERT INTO `todo` (`text`,`done`) VALUES (%s,%s)"
        val = (text, 0)
        mycursor.execute(sql, val)
        logger.debug("Commit changes to the database")
        mydb.commit()
        logger.debug("Invoke: def close_db(mydb)")
        close_db(mydb)
        return mycursor.lastrowid
    except Exception as error:
        logger.error(error)


def delete_todo_by_id(id):
    try:
        logger.debug('Invoke: def open_db()')
        mydb = open_db()
        logger.debug("Start db")
        mycursor = mydb.cursor()
        sql = "DELETE FROM todo where id=%s"
        val = (id,)
        mycursor.execute(sql, val)
        logger.debug("Commit changes to the database")
        mydb.commit()
        logger.debug("Invoke: def close_db(mydb)")
        close_db(mydb)
        return mycursor.rowcount
    except Exception as error:
        logger.error(error)


def update_todo_by_id(id, text, done):
    try:
        logger.debug('Invoke: def open_db()')
        mydb = open_db()
        logger.debug("Start db")
        mycursor = mydb.cursor()
        sql = "UPDATE todo SET `text` = %s, `done` = %s  WHERE id=%s"
        val = (text, done, id)
        mycursor.execute(sql, val)
        logger.debug("Commit changes to the database")
        mydb.commit()
        logger.debug("Invoke: def close_db(mydb)")
        close_db(mydb)
        # print(mycursor.rowcount, "record(s) affected")
        return id
    except Exception as error:
        logger.error(error)
