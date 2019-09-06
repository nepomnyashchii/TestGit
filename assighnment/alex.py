import pymongo
import mysql.connector


def getSQL():
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
    return sql


def executeSQL(sql):
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="coolspammail",
        passwd="coolspammail-pass",
        database="coolspammail"
    )
    mycursor = mydb.cursor()

    for i in mycursor.execute(sql, params=None, multi=True):
        print(mycursor.rowcount)
    # it = mycursor.execute(sql, params=None, multi=True)
    # for i in it:
    #     print(i)
    mydb.commit()





sql = getSQL()
print(sql)
executeSQL(sql)
