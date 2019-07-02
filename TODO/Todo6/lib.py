import json
import mysql.connector
import logger_module
logger = logger_module.setup_logger("todo-2lib")


def open_db():
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="coolspammail",
        passwd="coolspammail-pass",
        database="coolspammail"
    )
    return mydb

def get_all():
    """get flowdata from db."""

    try:
        logger.debug('Invoke def open_db()')
        mydb = open_db()
        logger.debug("Start db")
        mycursor = mydb.cursor()
        logger.debug("Start executing action for db")
        sql = "SELECT * FROM `todo`"
        mycursor.execute(sql)
        # this will extract row headers
        logger.debug("Collect list of tuples for all ids")
        rv = mycursor.fetchall()
        logger.debug("All obtained data from database" +str(rv))
        row_headers = [x[0] for x in mycursor.description]
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        logger.debug("Create dictionary with inserted row_headers from tuple" +str(json_data))
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
    return json_data


def get_todo_by_id(id):
    # myresult = ''
    try:
        logger.debug('Invoke def open_db()')
        mydb = open_db()
        logger.debug("Start db")
        mycursor = mydb.cursor()
        sql = "SELECT * FROM todo WHERE id = %s;"
        val = (id,)
        mycursor.execute(sql, val)
        # this will extract row headers
        logger.debug("Collect list of tuples for all ids")
        rv = mycursor.fetchall()
        logger.debug("All obtained data from database" +str(rv))
        row_headers = [x[0] for x in mycursor.description]
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        logger.debug("Create dictionary with inserted row_headers from tuples" +str(json_data))
        logger.debug("Close the database")
        mydb.close()
        return json_data
    except:
        print("Something went wrong with get_to_do_by_id")


def insert_todo(text):
    try:
        logger.debug('Invoke def open_db()')
        mydb = open_db()
        logger.debug("Start db")
        mycursor = mydb.cursor()
        sql = "INSERT INTO `todo` (`text`,`done`) VALUES (%s,%s)"
        val = (text, 0)
        mycursor.execute(sql, val)
        logger.debug("Commit changes to the database")
        mydb.commit()
        logger.debug("Close the database")
        mydb.close()
        return mycursor.lastrowid
    except:
        print("Something went wrong with insert_todo")


def delete_todo_by_id(id):
    try:
        logger.debug('Invoke def open_db()')
        mydb = open_db()
        logger.debug("Start db")
        mycursor = mydb.cursor()
        sql = "DELETE FROM todo where id=%s"
        val = (id,)
        mycursor.execute(sql, val)
        logger.debug("Commit changes to the database")
        mydb.commit()
        logger.debug("Close the database")
        mydb.close()
        return mycursor.rowcount
    except:
        print("Something went wrong with delete_todo_by_id")


def update_todo_by_id(id, text, done):
    try:
        logger.debug('Invoke def open_db()')
        mydb = open_db()
        logger.debug("Start db")
        mycursor = mydb.cursor()
        sql = "UPDATE todo SET `text` = %s, `done` = %s  WHERE id=%s"
        val = (text, done, id)
        mycursor.execute(sql, val)
        logger.debug("Commit changes to the database")
        mydb.commit()
        logger.debug("Close the database")
        mydb.close()
        # print(mycursor.rowcount, "record(s) affected")
        return id
    except:
        print("Something went wrong with updata_todo_by_id")
