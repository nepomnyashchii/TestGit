import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["sasha2"]
person1 = {
    "name": "alex",
    "phone": "234",
    "email" : "coolim@gmail.edu"}
    
person2= {"name" : "john",
    "phone": "123",
    "email":"rainboy@gmail.com"}

person3 ={
    "name": "mike",
    "phone": "567",
    "email": "milk@gmail.com"}

x = mycol.insert_many(person1, person2, person3)

print(x.inserted_id)


