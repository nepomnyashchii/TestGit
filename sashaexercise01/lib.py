import mysql.connector


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
    print(splited)
    action = splited[0]
    print(action)
    # action = actionline[0].split(":")[0]
    if action == 'news':
        return get_news(actionline)
    if action == 'norris':
        return get_norris(actionline)
    return {
            "action": action,

        }


def get_news(actionline):
    # splited = actionline[0].split(":")
    # count = int(splited[1])
    count= int(actionline[0].split(":")[1])
    # fetch data from internet here
    return {
        "news": [],
        "count": str(count)
    }


def get_norris(actionline):
    splited = actionline[0].split(":")
    count = int(splited[1])
    # fetch data from internet here
    return {
        "norris": [],
        "count": str(count)
    }

