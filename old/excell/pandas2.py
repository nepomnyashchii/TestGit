import sys
import pandas as pd


def print_as_table(data):
    for lineIndex in data.index:
        line_str = str(lineIndex) + ":\t"
        for columnName in data.columns:
            if columnName != 'OrderDate':
                line_str += columnName + "=" + \
                    str(data[columnName][lineIndex]) + "\t"
        print(line_str + "\n")


def print_as_csv(data):

    # print column names in first line
    first_line = ""
    for column_name in data.columns:
        first_line += column_name + ","
    print(first_line[:-1])
    # print values
    for line_index in data.index:
        line_str = ""
        for column_name in data.columns:
            line_str += str(data[column_name][line_index]) + ","
        print(line_str[:-1])


def print_as_sql(data):
    sql_templ = """
         INSERT INTO xxx (OrderDate,Region,Rep,Item,Units,Unit Cost,Total)
         VALUES ('%s', '%s', '%s', '%s', %s, %s, %s);"""
    for line_index in data.index:
        values = []
        for column_name in data.columns:
            values.append(data[column_name][line_index])
        print(sql_templ % tuple(values))


data = pd.read_excel('./data.xlsx', sheet_name='SalesOrders')


while 1:
    user_input = input("Select Format: 1:CSV, 2:Table, 3:SQL (0:exit):")
    if int(user_input) == 1:
        print_as_csv(data)
    if int(user_input) == 2:
        print_as_table(data)
    if int(user_input) == 3:
        print_as_sql(data)
    if int(user_input) == 0:
        sys.exit()
