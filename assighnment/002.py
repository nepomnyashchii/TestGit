import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["sasha1"]
myquery = {"names": "all"}
mydoc = mycol.find_one(myquery)
myresult=mydoc
myresult2 = myresult["list"]
print(myresult2)
table2 = []
for data in myresult2:
    result = data
    myphone = result["phone"]
    table2.append(myphone)


# mylist = [
#             {'user': 'Bot1', 'version': 0.11, 'items': 23, 'methods': 'standard', 'time': 1536304833437, 'logs': 'no', 'status': 'completed'},
#             {'user': 'Bot2', 'version': 0.15, 'items': 43, 'methods': 'standard', 'time': 2555645896453, 'logs': 'yes', 'status': 'cancelled'},
#             {'user': 'Bot3', 'version': 0.17, 'items': 63, 'methods': 'standard', 'time': 3265114687998, 'logs': 'yes', 'status': 'completed'}
#           ]

# for mydict in mylist:
#     placeholders = ', '.join(['%s'] * len(mydict))
#     columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in mydict.keys())
#     values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
#     sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('mytable', columns, values)
#     # print(sql)


    # f = open("/home/user/files/bots.sql", "a")
    # f.write(sql + '\n')




