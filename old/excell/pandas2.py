import sys
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
            host="db4free.net",
            user="coolspammail",
            passwd="coolspammail-pass",
            database="coolspammail"
        )

def print_as_sql(data):
    sql_templ = """
         INSERT INTO test_pandas (A,B)
         VALUES (%s, %s);"""
    for line_index in data.index:
        values = []
        for column_name in data.columns:
            values.append(data[column_name][line_index])
        print(sql_templ % tuple(values))


data = pd.read_excel('./alec.xlsx')

print_as_sql(data)
