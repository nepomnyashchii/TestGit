import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["customers"]

myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")