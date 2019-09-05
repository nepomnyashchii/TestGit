import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["sasha3"]
myquery = { "name": { "$regex": "a" } }
mydoc = mycol.find(myquery)
phone = []
name = []
email = []
for x in mydoc:
#   print(x)
  result = x["phone"]
  phone.append(result)
  result2 = x["name"]
  name.append(result2)
  result3 = x["email"]
  email.append(result3)
data = tuple(phone)
data1 = tuple(name)
data2 = tuple(email)
print(data)
print(data1)
print(data2)

