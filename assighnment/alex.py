import pymongo
import mysql.connector
client = pymongo.MongoClient(
    "mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["sasha3"]
myquery = {"name": {"$regex": "a"}}
mydocs = mycol.find(myquery)
sql = ''
for x in mydocs:
    sql += "INSERT INTO clients (name, phone, email) VALUES ('" + \
        x["name"]+"', '" + x["phone"] + "', '" + x["email"] + "');\n"
print(sql)


mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
)

mycursor = mydb.cursor()

mycursor.execute(sql, params=None, multi=True)

# for i in mycursor.execute(sql, params=None, multi=True):
#     print(i)

# it = mycursor.execute(sql, params=None, multi=True)
# for i in it:
#     print(i)

mydb.commit()
print(mycursor.rowcount)
