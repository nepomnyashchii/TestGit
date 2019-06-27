import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["customers"]

myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)