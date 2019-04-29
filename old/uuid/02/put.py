import mysql.connector

print("Please wait...")


msg = "privet"
exp = 600
pin = 1234
sid = "sdf sdfsdf sdfsdf sd fsd"

return_value=''

try:
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="coolspammail",
        passwd="coolspammail-pass",
        database="coolspammail"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO secret (id, msg, pin, exp) VALUES (%s, %s, %s, %s)"
    val = (sid, msg, pin, exp)
    mycursor.execute(sql, val)
    mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)
    return_value=sid

except:
    print("Something went wrong")

print('return_value:' + return_value)
