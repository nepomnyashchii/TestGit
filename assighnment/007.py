import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["sasha3"]
myquery = { "name": { "$regex": "a" } }
mydoc = mycol.find(myquery)
phone = []
for x in mydoc:
  print(x)
  result = x["phone"]
  print(result)
  phone.append(result)
print(phone)

