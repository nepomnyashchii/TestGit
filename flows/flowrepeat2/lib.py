import mysql.connector, requests, json

def get_flowdata(username, flow):
    myresult = " "
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
    splited= actionline.split(":")
    action = splited[0]
    if action == "news":
        return news_data (actionline)
    if action == "norris":
        return norris_data(actionline)

def news_data (actionline):
    splited = actionline.split(":")
    count =splited [1]
    return api_news(count)

def norris_data (actionline):
    splited = actionline.split(":")
    count = splited [1]
    return api_norris (count)

def api_news (count):
    news_information = requests.get(("https://newsapi.org/v1/articles?pageSize=3&source=hacker-news&apiKey=c39a26d9c12f48dba2a5c00e35684ecc"))
    return convert_news (news_information, count)

def api_norris (count):
    norris_information = requests.get(('http://api.icndb.com/jokes/random/' + str(count)))
    return convert_norris (norris_information, count)

def convert_news (news_information, count):
    obj_news = news_information.json()
    source_articles = obj_news["articles"]
    return_articles_list = []
    for source_article in source_articles[:count]:
        article = {
            "title": source_article["title"],
            "description": source_article["description"]
        }
        return_articles_list.append(article)

    return return_articles_list
    print(return_articles_list)





