import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://nepomnyashchii:natasha1977#5@cluster0-6p7nv.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
articles = db.articles
delete_articles = articles.delete_many({})
print(delete_articles.deleted_count, " articles deleted.")