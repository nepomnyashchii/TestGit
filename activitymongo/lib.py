import pymongo
import requests
import json
import logger_module

logger = logger_module.getModuleLogger('flowsapp.MYLIB')


def get_flowdata(s_name, s_flow):
    logger.debug("get_flowdata invoked with:" + s_name + " " + s_flow)
    """get flowdata from db."""
    myresult = ''
    try:
        dbURL="mongodb://coolspammail:coolspammailpass1!@ds261626.mlab.com:61626/aaa"
        myclient = pymongo.MongoClient(dbURL)
        mydb = myclient["aaa"]

        mycol = mydb["user"]

        s_name='alex'
        s_flow='goodmorning'

        myquery = { "name": s_name }
        mydoc = mycol.find(myquery, {"flows": 1 })
        if mydoc.count() > 0:
            x = mydoc[0]
            flows=x["flows"]
            for flow in flows:
                if flow.get(s_flow):
                    myresult = flow.get(s_flow)
                    print(myresult)
        else:
            print('data not found')
    except:
        logger.error('An error occured.')
    logger.debug("get_flowdata finished with:" + str(myresult))

    return myresult


def run_action(actionline):
    logger.debug('run_action invoked actionline: ' + actionline)
    splited = actionline.split(":")
    action = splited[0]
    if action == "news":
        return apinews_data(actionline)
    if action == "norris":
        return apinorris_data(actionline)
    if action == "thecocktail":
        return cocktail_data(actionline)
    if action == "weather":
        return weather_data(actionline)
    logger.error('action not implemented' + action)
    return {
        "action": action,
    }


def apinews_data(actionline):
    splited = actionline.split(":")
    count = int(splited[1])
    logger.debug("apinews_data invoked: " + str(count))
    response = requests.get(
        "https://newsapi.org/v1/articles?pageSize=3&source=hacker-news&apiKey=c39a26d9c12f48dba2a5c00e35684ecc")

    if response.status_code != 200:
        return {"error": response.json()}

    logger.debug("apinews_data news_results: " + str(response))
    return_articles_list = convert_news(response, count)
    logger.debug("apinews_data finished: " + str(return_articles_list))
    return return_articles_list


def apinorris_data(actionline):
    splited = actionline.split(":")
    count = int(splited[1])
    response = requests.get(
        'http://api.icndb.com/jokes/random/' + str(count))
    jokes = convert_norris(response)
    logger.debug("apinorris_data invoked: " + str(jokes))
    return jokes


def convert_news(news_results, count):
    news_obj = news_results.json()
    source_articles = news_obj["articles"]
    return_articles_list = []
    for source_lexus in source_articles[:count]:
        article = {
            "title": source_lexus["title"],
            "description": source_lexus["description"]
        }
        return_articles_list.append(article)
    logger.debug("convert_news finished: " + str(return_articles_list))
    return return_articles_list


def convert_norris(norris_results):
    obj = norris_results.json()
    source_list = obj["value"]
    return_list = []
    for source_item in source_list:
        return_list.append(source_item["joke"])
    logger.debug("convert norris finished: " + str(return_list))
    return return_list


def cocktail_data(actionline):
    response = requests.get(
        'https://www.thecocktaildb.com/api/json/v1/1/random.php')

    logger.debug(response)
    return response.json()


def weather_data(actionline):
    logger.debug('weather_data invoked' + actionline)
    splited = actionline.split(":")
    location = splited[1]
    logger.debug('weather_data location=' + location)
    # url = 'https://samples.openweathermap.org/data/2.5/weather?q=' + \
    #     location + '&appid=1bdcae6b7d23f180361c8878a965c9f8'
    appid = '1bdcae6b7d23f180361c8878a965c9f8'
    url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(
        location, appid)
    logger.debug('weather_data url=' + url)
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": response.json()}
    logger.debug(response)
    return response.json()
