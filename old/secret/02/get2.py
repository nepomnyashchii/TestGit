import mysql.connector
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

    sid = '47cafc3f-8cb2-46f9-ae9b-824b3b8f4ed0'
    pin = 12345

    sql = "SELECT msg FROM secret WHERE id =  %s AND pin = %s"
    params = (sid, int(pin))

    mycursor.execute(sql, params)

    myresult = mycursor.fetchone()
    return_value = myresult[0]
except:
    print("Record not found")

print(return_value)
