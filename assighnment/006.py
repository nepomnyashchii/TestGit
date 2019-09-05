import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["sasha3"]
# myquery = {"name": "alex"}
# myquery2 = {"name" : "john"}
# myquery3 = {"name" : "mike"}
for element in mycol.find():
  print(element)


