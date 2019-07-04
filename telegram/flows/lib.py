import mysql.connector
import requests
import json


def get_nice_text_from_flows(data):
    text = ''
    for idx, line in enumerate(data):
        actionline = line[0]
        actionTitle = actionline.split(":")[0]
        action_data = run_action(actionline)
        print(action_data)
        if actionTitle == "norris":
            text += '==== Jokes ====\n\n\n'
            for joke in action_data:
                text += joke + '\n\n'
            text += '\n\n\n\n'

        if actionTitle == "news":
            text += '==== News ====\n\n\n'
            for news in action_data:
                text += str(news) + '\n\n'
            text += '\n\n\n\n'

        if actionTitle == "thecocktail":
            text += '==== theCocktail ====\n\n\n'
            result = action_data["drinks"]
            for cocktail in result:
                result1=cocktail
            result2 = result1["strDrinkThumb"]
            text += json.dumps(result2)
            text += '\n\n\n\n'

        if actionTitle == "weather":
            text += '==== Weather ====\n\n\n'
            result = action_data["temperature"]
            result1 = "Temperature: " + str(result) + " K"
            text += json.dumps(result1)
            text += '\n\n\n\n'


        else:
            pass
        # text += "=====" + actionTitle + "=====\n\n" + \
        # json.dumps(action_data) + "\n\n\n\n"
    return text


def open_db():
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="coolspammail",
        passwd="coolspammail-pass",
        database="coolspammail"
    )
    return mydb


def close_db(mydb):
    mydb.close()


def get_flowdata(person, flow):
    """get flowdata from db."""
    myresult = ''
    try:
        mydb = open_db()
        mycursor = mydb.cursor()
        sql = """
            SELECT action
            FROM `flows` INNER JOIN users ON flows.user_id = users.id
            WHERE LOWER(users.name)=%s AND flows.name =%s
            ORDER BY action_order
        """
        val = (person, flow)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        close_db(mydb)
    except:
        "We are the champions"
    return myresult


def run_action(actionline):
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
    return {
        "action": action,
    }


def apinews_data(actionline):
    splited = actionline.split(":")
    count = int(splited[1])
    response = requests.get(
        "https://newsapi.org/v1/articles?pageSize=3&source=hacker-news&apiKey=c39a26d9c12f48dba2a5c00e35684ecc")
    if response.status_code != 200:
        return {"error": response.json()}
    return_articles_list = convert_news(response, count)
    return return_articles_list


def apinorris_data(actionline):
    splited = actionline.split(":")
    count = int(splited[1])
    url = 'http://api.icndb.com/jokes/random/' + str(count)
    response = requests.get(url)
    jokes = convert_norris(response, actionline)
    return jokes


def convert_news(news_results, count):
    news_obj = news_results.json()
    source_articles = news_obj["articles"]
    return_articles_list = []
    for source_article in source_articles[:count]:
        article = {
            "title": source_article["title"],
            "description": source_article["description"]
        }
        return_articles_list.append(article)
    return return_articles_list


def convert_norris(norris_results, actionline):
    obj = norris_results.json()
    source_list = obj["value"]
    splited = actionline.split(":")
    name_change = splited[2]
    return_list = []
    for source_item in source_list:
        changed_joke = source_item["joke"].replace("Chuck Norris", name_change)
        return_list.append(changed_joke)
    return return_list


def cocktail_data(actionline):
    response = requests.get(
        'https://www.thecocktaildb.com/api/json/v1/1/random.php')

    return response.json()


def weather_data(actionline):
    splited = actionline.split(":")
    location = splited[1]
    # url = 'https://samples.openweathermap.org/data/2.5/weather?q=' + \
    #     location + '&appid=1bdcae6b7d23f180361c8878a965c9f8'
    appid = '1bdcae6b7d23f180361c8878a965c9f8'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(
        location, appid)
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": response.json()}
    return convert_weather(response)

def convert_weather (weather_results):
    weather = weather_results.json()
    # source_data = weather["main"]
    return_data = {"temperature": weather["main"]["temp"],
    "pressure": weather["main"]["pressure"],
    "city name": weather["name"]}
    return return_data