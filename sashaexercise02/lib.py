import request

def get_news(list):
    news_data= request.get("https://newsapi.org/v1/articles?source=hacker-news&apiKey=c39a26d9c12f48dba2a5c00e35684ecc")
    newslist =[]
    for line in news_data:
        newsList.append()
def get_norris(list):
    norris_data=request.get(('http://api.icndb.com/jokes/random/1')
    norrislist=[]
    for line in norris_data:
        norrisList.append()






