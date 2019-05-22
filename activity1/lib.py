import mysql.connector
import requests
import json

def get_flowdata(username, flow):
    """get flowdata from db."""
    myresult = ''
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
    return myresult

def api_news (actionline):
    splited = actionline.split(":")
    action = splited[0]
    if action == "news":
        return get_news(actionline)
    if action == "norris":
        return norris_data(actionline)
    if action == "weather":
        return weather_data (actionline)
    return {"action: " + action}

def get_news (actionline):
    splited = actionline.split(":")
    action =splited[1]
    return get_apinews(count)

def norris_data (actionline):
    splited = actionline.split(":")
    action =splited[1]
    return get_norrisnews(count)

def weather_data(actionline):
    response = requests.get("https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=1bdcae6b7d23f180361c8878a965c9f8")
    return response.json()

def get_apinews(count:):
    listnews = []
    response


