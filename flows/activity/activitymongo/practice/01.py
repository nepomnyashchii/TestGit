
import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["flows"]
s_flow = {"goodmorning" : ["news:3", "norris:3", "cocktail-random", "weather:Brooklyn, NY"]}
s_name = {"Alex" : ["news:3", "norris:3", "cocktail-random", "weather:Brooklyn, NY"]}
result = {"flows": [s_flow, s_name]}
x = mycol.insert_one(result)

print(x.inserted_id)

