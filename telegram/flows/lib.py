import mysql.connector
import requests
import json
import logger_module


logger = logger_module.setup_logger("lib2")


def get_nice_text_from_flows(data):
    text = ''
    for idx, line in enumerate(data):
        actionline = line[0]
        actionTitle = actionline.split(":")[0]
        action_data = run_action(actionline)
        # print(action_data)
        if actionTitle == "norris":
            text+= '==== Jokes ====\n\n\n'
            for joke in action_data:
                text+= joke + '\n\n'
                print(joke)
                print(text)
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
                text += cocktail["strDrinkThumb"]
            text += '\n\n\n\n'

        if actionTitle == "weather":
            text += '==== Weather ====\n\n\n'
            result = action_data["temperature"]
            result1 = result-273.00
            # print(result1)
            result2 = round(result1)
            result3 = "Temperature: " + str(result2) + " degrees Celcius"
            text +=result3
            text += '\n\n\n\n'


        else:
            pass
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
    myresult = ''
    try:
        logger.debug('Invoke def open_db()')
        mydb = open_db()
        mycursor = mydb.cursor()
        logger.debug("Start executing action for db")
        sql = """
            SELECT action
            FROM `flows` INNER JOIN users ON flows.user_id = users.id
            WHERE LOWER(users.name)=%s AND flows.name =%s
            ORDER BY action_order
        """
        val = (person, flow)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        logger.debug("All obtained data: " + str(myresult))
        logger.debug("Invoke def close_db(mydb)")
        close_db(mydb)

    except IOError:
        logger.error('An error occured trying to read the file.')
    except ValueError:
        logger.error('Non-numeric data found in the file.')
    except ImportError:
        logger.error("NO module found")
    except EOFError:
        logger.error('Why did you do an EOF on me?')
    except KeyboardInterrupt:
        logger.error('You cancelled the operation.')
    except:
        logger.error('An error occured.')
    logger.debug("get_flowdata finished with: " + str(myresult))
    return myresult

def run_action(actionline):
    logger.debug("Invoke actionline: " + actionline)
    splited = actionline.split(":")
    action = splited[0]
    logger.debug("Action: " + str(splited))
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
    logger.debug("Invoke Apinews")
    splited = actionline.split(":")
    logger.debug("Apinews: " + str(splited))
    count = int(splited[1])
    logger.debug("Amount of news: " + str(count))
    response = requests.get(
        "https://newsapi.org/v1/articles?pageSize=3&source=hacker-news&apiKey=c39a26d9c12f48dba2a5c00e35684ecc")
    if response.status_code != 200:
        return {"error": response.json()}
    logger.debug("Apinews: " + str(response))
    return_articles_list = convert_news(response, count)
    logger.debug("Apinews_collected: " + str(return_articles_list))
    return return_articles_list


def apinorris_data(actionline):
    logger.debug("Invoke apinorris")
    splited = actionline.split(":")
    logger.debug("Apinorris: " + str(splited))
    count = int(splited[1])
    logger.debug("Amount of apinorris: " + str(count))
    url = 'http://api.icndb.com/jokes/random/' + str(count)
    response = requests.get(url)
    logger.debug("Apinorris: " + str(url))
    jokes = convert_norris(response, actionline)
    logger.debug("Apinorris_collected: " + str(jokes))
    return jokes


def convert_news(news_results, count):
    logger.debug("Invoke convert_news,apinews json conversion")
    news_obj = news_results.json()
    logger.debug("Convert_news, apinews: " + str(news_obj))
    source_articles = news_obj["articles"]
    logger.debug("Convert_news, apinews: " + str(source_articles))
    return_articles_list = []
    for source_article in source_articles[:count]:
        article = {
            "title": source_article["title"],
            "description": source_article["description"]
        }
        return_articles_list.append(article)
    logger.debug("Convert_news, apinews finished: " + str(return_articles_list))
    return return_articles_list


def convert_norris(norris_results, actionline):
    logger.debug("Invoke convert_norris,apinorris json conversion")
    obj = norris_results.json()
    logger.debug("Convert_norris_apinorris: " + str(obj))
    source_list = obj["value"]
    logger.debug("Convert_norris, apinorris: " + str(source_list))
    splited = actionline.split(":")
    name_change = splited[2]
    logger.debug("Convert_norris, apinorris new name: " + str(name_change))
    return_list = []
    for source_item in source_list:
        changed_joke = source_item["joke"].replace("Chuck Norris", name_change)
        return_list.append(changed_joke)
    logger.debug("Collect all data and name change" + str(return_list))
    return return_list


def cocktail_data(actionline):
    logger.debug("Invoke Cocktail_data")
    response = requests.get(
        'https://www.thecocktaildb.com/api/json/v1/1/random.php')
    logger.debug("Cocktail_data: " + str(response))
    return response.json()


def weather_data(actionline):
    logger.debug('Invoke weather_data' + actionline)
    splited = actionline.split(":")
    logger.debug("Weather_data: " + str(splited))
    location = splited[1]
    logger.debug("Weather_data: " + str(location))
    appid = '1bdcae6b7d23f180361c8878a965c9f8'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(
        location, appid)
    logger.debug('Weather_data url= ' + str(url))
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": response.json()}
    logger.debug("Weather data: " + str(response))
    return convert_weather(response)

def convert_weather (weather_results):
    logger.debug("Invoke convert weather_results")
    weather = weather_results.json()
    return_data = {"temperature": weather["main"]["temp"],
    "pressure": weather["main"]["pressure"],
    "city name": weather["name"]}
    logger.debug("Weather results" + str(return_data))
    return return_data