import mysql.connector
import requests
import json
import logger_module

logger = logger_module.getModuleLogger('flowsapp.MYLIB')


def get_flowdata(username, flow):
    logger.debug("get_flowdata invoked with:" + username + " " + flow)
    """get flowdata from db."""
    myresult = ''
    try:
        mydb = mysql.connector.connect(
            host="db4free.net",
            user="coolspammail",
            passwd="coolspammail-pass",
            database="coolspammail"
        )

        mycursor = mydb.cursor()
        sql = """
            SELECT action
            FROM `flows` INNER JOIN users ON flows.user_id = users.id
            WHERE LOWER(users.name)=%s AND flows.name =%s
            ORDER BY action_order
        """
        val = (username, flow)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
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
    logger.debug("get_flowdata finished with:" + str(myresult))
    return myresult


def run_action(actionline):
    logger.debug('run_action invoked actionline: ' + actionline)
    splited = actionline.split(":")
    action = splited[0]
    if action == "news":
        return news_data(actionline)
    if action == "norris":
        return norris_data(actionline)
    if action == "thecocktail":
        return cocktail_data(actionline)
    if action == "weather":
        return weather_data(actionline)
    logger.error('action not implemented' + action)
    return {
        "action": action,
    }


def news_data(actionline):
    splited = actionline.split(":")
    count = int(splited[1])
    return apinews_data(count)


def norris_data(actionline):
    splited = actionline.split(":")
    count = int(splited[1])
    return apinorris_data(count)


def apinews_data(count):
    print("apinews_data invoked: " + str(count))
    response = requests.get(
        "https://newsapi.org/v1/articles?pageSize=3&source=hacker-news&apiKey=c39a26d9c12f48dba2a5c00e35684ecc")

    if response.status_code != 200:
        return {"error": response.json()}

    print("apinews_data news_results: " + str(response))
    return_articles_list = convert_news(response, count)
    print("apinews_data invoked: " + str(return_articles_list))
    return return_articles_list


def apinorris_data(count):
    response = requests.get(
        'http://api.icndb.com/jokes/random/' + str(count))
    return_articles_list = convert_norris(response)
    return return_articles_list


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

    return return_articles_list


def convert_norris(norris_results):
    obj = norris_results.json()
    source_list = obj["value"]
    return_list = []
    for source_item in source_list:
        return_list.append(source_item["joke"])
    return return_list


def cocktail_data(actionline):
    response = requests.get(
        'https://www.thecocktaildb.com/api/json/v1/1/random.php')

    print(response)
    return response.json()


def weather_data(actionline):
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/forecast?q=Brooklyn&APPID=1bdcae6b7d23f180361c8878a965c9f8')
    if response.status_code != 200:
        return {"error": response.json()}
    return response.json()
