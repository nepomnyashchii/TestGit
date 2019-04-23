import mysql.connector
import time
import uuid

print("Please wait...")


msg = "time3"
exp = 600
pin = 1234
sid = str(uuid.uuid4())
mytime=time.strftime('%Y-%m-%d %H:%M:%S')
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
    val = (sid, msg, pin, exp, mytime)
    mycursor.execute(sql, val)
    mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)
    return_value = sid

except:
    print("Something went wrong")

print('return_value:' + return_value)
