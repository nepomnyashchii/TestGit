import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["customers"]
for x in mycol.find({},{ "name": 1, "address": 0 }):
# mistake cannot be both inclusion and exclusion
  print(x)