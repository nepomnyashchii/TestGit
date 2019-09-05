import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["sasha"]
result = {"names":
        [
            {
    "name": "alex",
    "phone": "234",
    "email" : "coolim@gmail.edu"},
    {"name" : "john",
    "phone": "123",
    "email":"rainboy@gmail.com"},
    {"name": "mike",
    "phone": "567",
    "email": "milk@gmail.com"}]
    }
x = mycol.insert_one(result)

print(x.inserted_id)

