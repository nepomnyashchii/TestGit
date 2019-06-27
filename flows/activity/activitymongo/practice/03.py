import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
mycol = db["flows"]
result = {
    "name": "alex",
    "phone": "234",
    "flows": [
        {
            "goodmorning": [
                "news:3",
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
}
x = mycol.insert_one(result)

print(x.inserted_id)
