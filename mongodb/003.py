import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
articles = db.articles
query = { "author": "Derrick Mwiti" }
new_author = { "$set": { "author": "John David" } }

articles.update_one(query, new_author)

for article in articles.find():
  print(article)
