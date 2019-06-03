import pymongo

dbURL="mongodb://coolspammail:coolspammailpass1!@ds261626.mlab.com:61626/aaa"
myclient = pymongo.MongoClient(dbURL)
mydb = myclient["aaa"]

# print(myclient.list_database_names())

# mycol = mydb["customers"]
# print(mydb.list_collection_names())

# collist = mydb.list_collection_names()
# if "user" in collist:
#   print("The collection exists.")



# mycol = mydb["customers"]
# mydict = {
#     "name": "Joh1",
#     "address":
#     "Highway 37"
#     }
# x = mycol.insert_one(mydict)
# print(x.inserted_id)



# mycol = mydb["customers"]

# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]

# x = mycol.insert_many(mylist)

# #print list of the _id values of the inserted documents:
# print(x.inserted_ids)

mycol = mydb["user"]

# x = mycol.find_one()
# print(x)


# for x in mycol.find():
#   print(x)


# for x in mycol.find({},{ "name": "Alex" }):
#   print(x)

# for x in mycol.find({},{  "phone": 0 }):
#   print(x)

# myquery = { "name": "alex" }
# mydoc = mycol.find(myquery,{"flows": 1 })
# for x in mydoc:
#   print(x)

s_name='alex'
s_flow='goodmorning'

myquery = { "name": s_name }
mydoc = mycol.find(myquery, {"flows": 1 })
if mydoc.count() > 0:
    x = mydoc[0]
    flows=x["flows"]
    for flow in flows:
        if flow.get(s_flow):
            print(flow.get(s_flow))
else:
    print('data not found')




# mycol = mydb["customers"]
# myquery = { "address": { "$gt": "C" } }
# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)


# myquery = { "name": "Alex", "phone": {"$gt":"2"}}
# mydoc = mycol.find(myquery,{"flows": 1 })
# for x in mydoc:
#   print(x)