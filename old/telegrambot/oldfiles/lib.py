import json
import mysql.connector
import telebot




def open_db():
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="coolspammail",
        passwd="coolspammail-pass",
        database="coolspammail"
    )
    return mydb

def close_db(mydb):
    mydb.close()


def get_all():
    """get flowdata from db."""
    mydb = open_db()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM `todo`"
    mycursor.execute(sql)
        # this will extract row headers
    rv = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    close_db(mydb)
    return json_data


# def get_todo_by_id(id):
#     # myresult = ''
#     try:
#         mydb = open_db()
#         mycursor = mydb.cursor()
#         sql = "SELECT * FROM todo WHERE id = %s;"
#         val = (id,)
#         mycursor.execute(sql, val)
#         # this will extract row headers
#         logger.debug("Collect list of tuples for all ids")
#         rv = mycursor.fetchall()
#         logger.debug("All obtained data from database" +str(rv))
#         row_headers = [x[0] for x in mycursor.description]
#         json_data = []
#         for result in rv:
#             json_data.append(dict(zip(row_headers, result)))
#         close_db(mydb)
#         return json_data
#     except IOError:
#         logger.error('An error occured trying to read the file.')
#     except ValueError:
#         logger.error('Non-numeric data found in the file.')
#     except ImportError:
#         logger.error("NO module found")
#     except EOFError:
#         logger.error('Why did you do an EOF on me?')
#     except KeyboardInterrupt:
#         logger.error('You cancelled the operation.')
#     except:
#         logger.debug('An error occured.')


