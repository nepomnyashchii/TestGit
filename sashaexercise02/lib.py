import requests
import json


def get_news(count):
    news_data = requests.get(
        "https://newsapi.org/v1/articles?pageSize=3&source=hacker-news&apiKey=c39a26d9c12f48dba2a5c00e35684ecc")
    return_articles_list = convert_news(news_data, count)
    return return_articles_list


def get_norris(count):
    norris_data = requests.get(
        'http://api.icndb.com/jokes/random/' + str(count))
    return_list = convert_norris(norris_data)
    return return_list


def convert_news(news_data, count):
    news_obj = news_data.json()
    source_articles = news_obj["articles"]
    return_articles_list = []
    for source_article in source_articles[:count]:
        article = {
            "title": source_article["title"],
            "description": source_article["description"]
        }
        return_articles_list.append(article)

    return return_articles_list


def convert_norris(norris_data):
    obj = norris_data.json()
    source_list = obj["value"]
    return_list = []
    for source_item in source_list:
        return_list.append(source_item["joke"])
    return return_list
