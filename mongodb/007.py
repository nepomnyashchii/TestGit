import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
db.inventory.insert_many([
    {"item": "journal",
     "qty": 25,
     "tags": ["blank", "red"],
     "size": {"h": 14, "w": 21, "uom": "cm"}},
    {"item": "mat",
     "qty": 85,
     "tags": ["gray"],
     "size": {"h": 27.9, "w": 35.5, "uom": "cm"}},
    {"item": "mousepad",
     "qty": 25,
     "tags": ["gel", "blue"],
     "size": {"h": 19, "w": 22.85, "uom": "cm"}}])

cursor = db.inventory.find({})


# db.collection.insertOne()	Inserts a single document into a collection.
# db.collection.insertMany()	db.collection.insertMany() inserts multiple documents into a collection.
# db.collection.insert()