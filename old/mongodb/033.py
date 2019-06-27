import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["customers"]
myquery = {"name" : "alex"}
newvalues = { "$set": {
    "name": "alex",
    "phone2": "345",
    "phone": "234",
    "flows": [
        {
            "goodmorning": [
                "news:10",
                "norris:3",
                "coctail:random",
                "weather:Brooklyn, NY"
            ]
        },
        {
            "hi": [
                "news:3",
                "norris:3",
                "coctail:random",
                "weather:Brooklyn, NY"
            ]
        }
    ]
} }
mycol.update_one(myquery,newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)