import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["customers"]
# You can update a record, or document as it is called in MongoDB, by using the update_one() method.
# The first parameter of the update_one() method is a query object defining which document to update.
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)