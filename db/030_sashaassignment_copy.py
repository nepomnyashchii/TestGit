# import mysql.connector
# import uuid
# def put_secret(msg, exp, pin):
#     Msg=str(msg)
#     Exp =int(exp)
#     Pin = int(pin)
#     uuid.uuid4()
# mydb = mysql.connector.connect(
#     host="db4free.net",
#     user="coolspammail",
#     passwd="coolspammail-pass",
#     database="coolspammail"
#     )
# mycursor = mydb.cursor()
# sql = "INSERT INTO secrets (put_secret) VALUES (%s, %s, %s)"
# val = ("John", 23, 32)

# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")
# #  return uuid on success on fail return '' (empty string)
def put_secret(msg, exp, pin):
    print(msg, exp, pin)
put_secret ("privet", 600, 1234)
import uuid
my_uuid = uuid.uuid4()
print(my_uuid)
def get_secret(pin, my_uuid):
    print(pin, my_uuid)
    return "ura"
msg= get_secret(1234, "fakeuuid")
print(msg)





