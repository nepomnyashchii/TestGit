from sqlalchemy.engine import create_engine
import mysql.connector


mydb = mysql.connector.connect(
    host="db4free.net",
    user="coolspammail",
    passwd="coolspammail-pass",
    database="coolspammail")

c = mydb.cursor()

c.execute('''
          CREATE TABLE rambo
          (id INTEGER PRIMARY KEY, name varchar(250) NOT NULL)
          ''')
c.execute('''
          CREATE TABLE rambo2
          (id INTEGER PRIMARY KEY, street_name varchar(250), street_number varchar(250),
           post_code varchar(250) NOT NULL, rambo2_id INTEGER NOT NULL,
           FOREIGN KEY(rambo2_id) REFERENCES rambo(id))
          ''')

c.execute('''
          INSERT INTO rambo VALUES(1, 'pythoncentral')
          ''')
c.execute('''
          INSERT INTO rambo2 VALUES(1, 'python road', '1', '00000', 1)
          ''')
mydb.commit()
mydb.close()