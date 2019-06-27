import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["flows"]
x = mycol.find_one()
print(x)
flows = x ["flows"]
print(flows)
s_flow = {"goodmorning" : ["news:3", "norris:3", "cocktail-random", "weather:Brooklyn, NY"]}
print(s_flow["goodmorning"])

