import pymongo
import dns
import requests
import json
import logger_module
import config

logger = logger_module.getModuleLogger('flowsapp.MYLIB')


def get_flowdata(user_name, user_flow):
    myresult = None
    try:
        logger.debug("get_flowdata invoked :" + user_name + " " + user_flow)
        """get flowdata from db."""
        client = pymongo.MongoClient(config.MongoClient)
        db = client["test"]
        mycol = db["flows"]
        myquery = {"name": user_name}
        mydoc = mycol.find_one(myquery)
        if (mydoc is None):
            logger.debug("My query returned None")
            return None
        logger.debug("My query returned" + str(mydoc))
        data = mydoc
        logger.debug("Query data from the database: " + str(data))
        flows = data["flows"]
        logger.debug("Queery data for flows" + str(flows))
        for flow in flows:
            if flow.get(user_flow):
                myresult = flow.get(user_flow)
        logger.debug("get_flowdata finished with:" + str(myresult))
    except Exception as error:
        logger.error(error)
    return myresult


def run_action(actionline):
    logger.debug('Run_action invoked actionline: ' + str(actionline))
    splited = actionline.split(":")
    action = splited[0]
    try:
        if action == "news":
            return apinews_data(actionline)
        if action == "norris":
            return apinorris_data(actionline)
        if action == "coctail":
            return cocktail_data(actionline)
        if action == "weather":
            return weather_data(actionline)
        logger.error("Action is not implemented: " + action)
    except Exception as error:
        logger.error(error)
        return {
            "action": action,
        }


def apinews_data(actionline):
    try:
        splited = actionline.split(":")
        logger.debug("Apinews_data: " + str(splited))
        count = int(splited[1])
        logger.debug("Apinews_data: " + str(count))
        response = requests.get(
            "https://newsapi.org/v1/articles?pageSize=3&source=hacker-news&apiKey=c39a26d9c12f48dba2a5c00e35684ecc")

        if response.status_code != 200:
            return {"error": response.json()}

        return_articles_list = convert_news(response, count)
        logger.debug("apinews_data result: " + str(return_articles_list))
        return return_articles_list
    except Exception as error:
        logger.error(error)


def apinorris_data(actionline):
    try:
        splited = actionline.split(":")
        logger.debug("Apinorris_data: " + str(splited))
        count = int(splited[1])
        logger.debug("Apinorris_data: " + str(count))
        response = requests.get(
            'http://api.icndb.com/jokes/random/' + str(count))
        jokes = convert_norris(response)
        logger.debug("apinorris_data_results: " + str(jokes))
        return jokes
    except Exception as error:
        logger.error(error)


def convert_news(news_results, count):
    try:
        news_obj = news_results.json()
        logger.debug("Convert_news, apinews: " + str(news_obj))
        source_articles = news_obj["articles"]
        logger.debug("Convert_news, api_news: " + str(source_articles))
        return_articles_list = []
        for source_article in source_articles[:count]:
            article = {
                "title": source_article["title"],
                "description": source_article["description"]
            }
            return_articles_list.append(article)
        logger.debug("Convert_news, apinews results: " +
                     str(return_articles_list))
        return return_articles_list
    except Exception as error:
        logger.error(error)


def convert_norris(norris_results):
    try:
        obj = norris_results.json()
        logger.debug("Convert_norris, norris_results: " + str(obj))
        source_list = obj["value"]
        return_list = []
        for source_item in source_list:
            return_list.append(source_item["joke"])
        logger.debug("convert norris finished: " + str(return_list))
        return return_list
    except Exception as error:
        logger.error(error)


def cocktail_data(actionline):
    try:
        response = requests.get(
            'https://www.thecocktaildb.com/api/json/v1/1/random.php')
        logger.debug("Cocktail_data" + str(response))
        return response.json()
    except Exception as error:
        logger.error(error)


def weather_data(actionline):
    try:
        logger.debug("Weather_data invoked: " + actionline)
        splited = actionline.split(":")
        logger.debug("Weather_data" + str(splited))
        location = splited[1]
        logger.debug('Weather_data location=' + location)
        appid = '1bdcae6b7d23f180361c8878a965c9f8'
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(
            location, appid)
        logger.debug('weather_data url=' + url)
        response = requests.get(url)
        if response.status_code != 200:
            return {"error": response.json()}
        logger.debug("Weather_data: " + str(response))
        return convert_weather(response)
    except Exception as error:
        logger.error(error)


def convert_weather(weather_data):
    try:
        weather = weather_data.json()
        logger.debug("weather_data" + str(weather))
        return_data = {"temperature": weather["main"]["temp"],
                       "pressure": weather["main"]["pressure"],
                       "city name": weather["name"]}
        logger.debug("weather data" + str(return_data))
        return return_data
    except Exception as error:
        logger.error(error)
