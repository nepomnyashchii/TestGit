import requests


def get_news(count):
    news_data = requests.get(
        "https://newsapi.org/v1/articles?pageSize=3&source=hacker-news&apiKey=c39a26d9c12f48dba2a5c00e35684ecc")
    return news_data.json()


def get_norris(count):
    norris_data = requests.get(
        'http://api.icndb.com/jokes/random/' + str(count))
    return norris_data.json()

