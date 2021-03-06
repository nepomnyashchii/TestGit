import mysql.connector, requests, json


def get_mixedtables(username, flow):
    myresult = ''

    # mydb = mysql.connector.connect(
    #     host="db4free.net",
    #     user="coolspammail",
    #     passwd="coolspammail-pass",
    #     database="coolspammail"
    # )
    # mycursor = mydb.cursor()
    # sql = """SELECT action
    #         FROM `flows` INNER JOIN users ON flows.user_id = users.id
    #         WHERE LOWER(users.name)=%s AND flows.name =%s
    #         ORDER BY action_order
    #         """
    # # NEW
    # val = (username, flow)
    # mycursor.execute(sql, val)
    # # old
    # # mycursor.execute(sql)

    # myresult = mycursor.fetchall()

    # return (myresult)

def run_action(actionline):
    splited = actionline[0].split(":")
    action = actionline[0].split(":")[0]
    if action == 'news':
        return get_news(actionline)
    if action == 'norris':
        return get_norris(actionline)
    return {
            "action": action,

        }

def get_news(actionline, count):
    splited = actionline[0].split(":")
    count= int(actionline[0].split(":")[1])
    news_data = requests.get(
        "https://newsapi.org/v1/articles?pageSize=3&source=hacker-news&apiKey=c39a26d9c12f48dba2a5c00e35684ecc")

    return {
        "news": [news_data],
        "count": str(count)
    }


def get_norris(actionline, count):
    splited = actionline[0].split(":")
    count = int(splited[1])
    norris_data = requests.get(
        'http://api.icndb.com/jokes/random/' + str(count))
    return {
        "norris": [norris_data],
        "count": str(count)
    }

# def get_news(count):
#     news_data = requests.get(
#         "https://newsapi.org/v1/articles?pageSize=3&source=hacker-news&apiKey=c39a26d9c12f48dba2a5c00e35684ecc")
#     return news_data.json()

# def get_norris(count):
#     norris_data = requests.get(
#         'http://api.icndb.com/jokes/random/' + str(count))
#     # norris=json.loads(norris_data.json())
#     # return norris["value"]
#     return norris_data.json()


