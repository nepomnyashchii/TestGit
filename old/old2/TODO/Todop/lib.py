import mysql.connector



mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
)

def get_all():
    """get flowdata from db."""
    myresult = ''
    try:
        mycursor = mydb.cursor()
        sql = "SELECT * FROM `todo`"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
    except: print("Something went wrong in get_all")
    return myresult

def get_id(id):
    # myresult = ''
    try:
        mycursor = mydb.cursor()
        sql = "SELECT * FROM todo WHERE id = %s;"
        val = (id,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
    except: print("Something went wrong with get_to_do_by_id")
    return myresult
