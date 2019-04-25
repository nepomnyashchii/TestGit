import uuid
import mysql.connector
import datetime

def put_secret(msg, pin, exp, created):
    """put secret into db table."""
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
        print("1 record inserted, ID:", mycursor)
        return_value = sid

    except:
        print("Something went wrong")

    return return_value


def get_secret(sid, pin):
    """get secret from db."""
    print(sid, pin)

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

        sql = "SELECT msg,created, exp FROM secret WHERE id =  %s AND pin = %s"
        params = (sid, int(pin))
        mycursor.execute(sql, params)
        myresult = mycursor.fetchone()
        return_value = myresult[0]
        mytime=myresult[1]
        exp=myresult[2]
        newtime = mytime + datetime.timedelta(0, exp)
        current_time = datetime.datetime.now()

        if newtime < current_time:
            return_value=''
    except:
        print("Record not found")

    print(return_value)

# def del_secret(sid, pin):
#     """del secret from db."""
#     print(sid, pin)

#     print("Please wait...")
#     return_value = ''
#     try:
#         mydb = mysql.connector.connect(
#             host="db4free.net",
#             user="coolspammail",
#             passwd="coolspammail-pass",
#             database="coolspammail"
#         )
#         mycursor = mydb.cursor()

#         # DELETE FROM secret WHERE id = '5d025a4c-5991-457d-a8f9-3e27de288b19' AND pin = 1234

#         sql = "DELETE FROM secret WHERE id =  %s AND pin = %s"
#         params = (sid, int(pin))
#         mycursor.execute(sql, params)
#         myresult = mycursor.fetchone()
#         print(myresult)
#         return_value = myresult[0]
#     except:
#         print("Record not found")

#     return return_value