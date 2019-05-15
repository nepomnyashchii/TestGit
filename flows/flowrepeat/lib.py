import mysql.connector
import requests
import json


def get_flowdata(username, flow):
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

    return myresult


def run_action (actionline):
    splited = actionline.split(":")
    action = splited[0]
    if action == "news":
        return news_data(actionline)
    if action == "norris":
        return norris_data(actionline)

def news_data(actionline):
    splited = actionline.split(":")
    count = int(splited[1])
    return apinews_data(count)


def norris_data(actionline):
    splited = actionline.split(":")
    count = int(splited[1])
    return apinorris_data (count)


def apinews_data(count):
    news_results = requests.get("https://newsapi.org/v1/articles?pageSize=3&source=hacker-news&apiKey=c39a26d9c12f48dba2a5c00e35684ecc")
    return_articles_list = convert_news(news_results, count)
    return return_articles_list

def apinorris_data(count):
    norris_results =requests.get('http://api.icndb.com/jokes/random/' + str(count))
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

def api_weather():
    weather_data = requests.get()
    return weather_data

