import pymongo
import dns
import mysql.connector
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["sasha3"]
myquery = { "name": { "$regex": "a" } }
mydoc = mycol.find(myquery)
phone = []
name = []
email = []
for x in mydoc:
#   print(x)
  result = x["phone"]
  phone.append(result)
  result2 = x["name"]
  name.append(result2)
  result3 = x["email"]
  email.append(result3)
first = [name[0],phone[0],email[0]]
second = [name[1], phone[1], email[1]]
data = tuple(first)
data1 = tuple(second)
print(data)
print(data1)
# print(data)
# print(data1)
# print(data2)

mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
    )
mycursor = mydb.cursor()

sql = "INSERT INTO clients (name, phone, email) VALUES (%s, %s, %s)"
val = data1

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")





