import mysql.connector

def get_mixedtables(username, flow):
    myresult = ''

    mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail"
    )
    mycursor = mydb.cursor()
    sql = " SELECT action ,action_order as a_order
            FROM `flows` INNER JOIN users ON flows.user_id = users.id
            WHERE LOWER(users.name)=%s AND flows.name =%s
            ORDER BY action_order"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return (myresult)





