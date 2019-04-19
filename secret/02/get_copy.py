import mysql.connector
print("Please wait...")
try:
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="coolspammail",
        passwd="coolspammail-pass",
        database="coolspammail"
    )
    mycursor = mydb.cursor()

    sid = 'cc27a6dc-2e22-4a71-8a7f-4d104d2abad4'
    pin = 12345


    sql = "SELECT * FROM secret WHERE id =  %s AND pin = %s"
    params = (sid, int(pin))

    mycursor.execute(sql, params)


    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
except:
    print ("Something went Wrong")

