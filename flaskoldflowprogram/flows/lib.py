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


def run_action(actionline):
    splited = actionline.split(":")
    action = splited[0]
    if action == 'news':
        return run_news_action(actionline)
    if action == 'norris':
        return run_norris_action(actionline)
    return {
        "action": action,
    }


def run_news_action(actionline):
    splited = actionline.split(":")
    count = int(splited[1])
    return get_news(count)


def run_norris_action(actionline):
    splited = actionline.split(":")
    count = int(splited[1])
    return get_norris(count)


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
