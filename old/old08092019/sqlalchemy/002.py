from sqlalchemy.engine import create_engine
import mysql.connector


mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail")

c = mydb.cursor()

c.execute('SELECT * FROM rambo')
print (c.fetchall())
c.execute('SELECT * FROM rambo2')
print (c.fetchall())
mydb.close()