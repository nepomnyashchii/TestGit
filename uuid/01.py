import uuid
my_uuid = uuid.uuid4()
print(my_uuid)
import mysql.connector
mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
    )
mycursor = mydb.cursor()
def put_secret(msg, exp, pin):
    print(msg, exp, pin)
    sql = "INSERT INTO secret (id, msg, pin, exp) VALUES (%s, %s, %s, %s)" ('', 'ggg', '1234', '600')
    val = ('monkey', 'apple', 1234, 600, 2007)

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")
put_secret ("privet", 600, 1234)

def get_secret(pin, my_uuid):
    print(pin, my_uuid)
    return "ura"
msg= get_secret(1234, "fakeuuid")
print(msg)
-