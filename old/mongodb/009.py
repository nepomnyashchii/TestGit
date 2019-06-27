import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

db.inventory.update_many(
    {"item": "paper"},
    {"$set": {"size.uom": "cm", "status": "P"},
     "$currentDate": {"lastModified": True}})
