import mysql.connector


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
            SELECT action ,action_order as a_order
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
    splited = actionline[0].split(":")
    action = splited[0]
    if action == 'news':
        return get_news(actionline)
    if action == 'norris':
        return get_norris(actionline)
    return {
        "action": action,
    }


def get_news(actionline):
    splited = actionline[0].split(":")
    count = int(splited[1])
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
