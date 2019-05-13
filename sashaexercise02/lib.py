import requests


def get_news(count):
    news_data = requests.get(
        "https://newsapi.org/v1/articles?pageSize=3&source=hacker-news&apiKey=c39a26d9c12f48dba2a5c00e35684ecc")
    return news_data.json()
    # newslist = []
    # for line in news_data:
    #     newsList.append()


# def get_norris(list):
#     norris_data = request.get(('http://api.icndb.com/jokes/random/1')
#     norrislist=[]
#     for line in norris_data:
#         norrisList.append()




news_count=4
simpleList=[]
news=get_news(news_count)
simpleList.append(news)
print(simpleList)
