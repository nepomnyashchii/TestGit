import mysql.connector


mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
)

def insert_furniture(chairs, tables):
    mycursor = mydb.cursor()
    sql = "INSERT INTO `furniture` (`chairs`,`tables`) VALUES (%s, %s)"
    val = (chairs, tables)
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.lastrowid

def get_everything():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM `furniture`"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult


def get_furniture_by_id(id):
    myresult = ''
    mycursor = mydb.cursor()
    sql = "SELECT * FROM furniture WHERE id = %s;"
    val = (id,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    return myresult


def update_furniture_by_id(id, chairs, tables):
    myresult = ""
    mycursor = mydb.cursor()
    sql = "UPDATE furniture SET `chairs` = %s, `tables` = %s  WHERE id=%s"
    val = (chairs, tables, id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    return myresult


def delete_furniture_by_id(id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM furniture where id= %s"
    val =(id,)
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.rowcount

















