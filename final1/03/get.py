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

    sid = 'b28761c2-0ac8-4414-abf8-875378a5dfd1'
    pin = 1234

    sql = "SELECT msg, created ,exp FROM secret WHERE id =  %s AND pin = %s"
    params = (sid, int(pin))

    mycursor.execute(sql, params)
    myresult = mycursor.fetchone()
    # print(myresult)

    return_value = myresult[0]
    dbtime = myresult[1]
    exp = myresult[2]
    exp = 100000
    newtime = dbtime + datetime.timedelta(0, exp)
    current_time = datetime.datetime.now()

    if newtime < current_time:
        return_value=''

except:
    print("Record not found")

print(return_value)