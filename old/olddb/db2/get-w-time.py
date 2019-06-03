import mysql.connector
import datetime
import time

print("Please wait...")
return_value = ''
try:
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="coolspammail",
        passwd="coolspammail-pass",
        database="coolspammail"
    )
    mycursor = mydb.cursor()

    sid = '79346fb4-c51d-466f-9fe3-93c4fbe1f8b2'
    pin = 1234

    sql = "SELECT msg, created ,exp FROM secret WHERE id =  %s AND pin = %s"
    params = (sid, int(pin))

    mycursor.execute(sql, params)
    myresult = mycursor.fetchone()
    # print(myresult)

    return_value = myresult[0]
    dbtime = myresult[1]
    exp = myresult[2]
    # exp = 6000
    newtime = dbtime + datetime.timedelta(0, exp)
    current_time = datetime.datetime.now()

    if newtime < current_time:
        return_value=''

except:
    print("Record not found")

print(return_value)
