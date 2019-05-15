import mysql.connector
import requests
import json


def get_flowdata(username, flow):
    print("get_flowdata invoked with:" + username + " " + flow)
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
        print('An error occured trying to read the file.')
    except ValueError:
        print('Non-numeric data found in the file.')
    except ImportError:
        print("NO module found")
    except EOFError:
        print('Why did you do an EOF on me?')
    except KeyboardInterrupt:
        print('You cancelled the operation.')
    except:
        print('An error occured.')
    print("get_flowdata finished with:" + str(myresult))
    return myresult


def run_action(actionline):
    splited = actionline.split(":")
    action = splited[0]
    if action == "news":
        return news_data(actionline)
    if action == "norris":
        return norris_data(actionline)
    # if action == "thecocktail":
    #     return cocktail_data(actionline)
    # if action == "weather":
    #     return weather_data(actionline)
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
    news_results = requests.get(
        "https://newsapi.org/v1/articles?pageSize=3&source=hacker-news&apiKey=c39a26d9c12f48dba2a5c00e35684ecc")

    if news_results.status_code != 200:
        return {"error": news_results.json()}

    print("apinews_data news_results: " + str(news_results))
    return_articles_list = convert_news(news_results, count)
    print("apinews_data invoked: " + str(return_articles_list))
    return return_articles_list


def apinorris_data(count):
    norris_results = requests.get(
        'http://api.icndb.com/jokes/random/' + str(count))
    return_articles_list = convert_norris(norris_results)
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
    cocktail_message = requests.get(
        'https://www.thecocktaildb.com/api/json/v1/1/random.php')
    return cocktail_message

# def weather_data (actionline):
#     weather_data = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=Brooklyn&APPID=1bdcae6b7d23f180361c8878a965c9f8')
#     return weather_data


# def api_weather():
#     weather_data = requests.get()
#     return weather_data
