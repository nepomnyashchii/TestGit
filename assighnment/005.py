import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["sasha3"]
myquery = {"name": "alex"}
myquery2 = {"name" : "john"}
myquery3 = {"name" : "mike"}
mydoc = mycol.find_one(myquery)
mydoc2 = mycol.find_one(myquery2)
mydoc3  = mycol.find_one(myquery3)
print(mydoc)
print(mydoc2)
print(mydoc3)