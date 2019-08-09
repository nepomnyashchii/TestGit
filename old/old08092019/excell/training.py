import sys
import pandas as pd

data = pd.read_excel('./data.xlsx', sheet_name='SalesOrders')

def print_as_table (data):
    for line_Index in data.index:
        data_str = str(line_Index) + '\t'
        # print(data_str)
        for columnName in data.columns:
            data_str += columnName + "=" + str(data[columnName][line_Index]) + '\t'
        print(data_str)

print_as_table(data)

def print_as_cvs(data):
    first_line = ""
    for column_name in data.columns:
        first_line += column_name + ","
    print(first_line[:-1])
    for line_index in data.index:
        line_str = ""
        for column_name in data.columns:
            line_str += str(data[column_name][line_index]) + ","
        print(line_str[:-1])

# print_as_cvs (data)

def print_as_sql(data):
    sql_templ = """
         INSERT INTO xxx (OrderDate,Region,Rep,Item,Units,Unit Cost,Total)
         VALUES ('%s', '%s', '%s', '%s', %s, %s, %s);"""
    for line_index in data.index:
        values = []
        for column_name in data.columns:
            values.append(data[column_name][line_index])
        # print(sql_templ)
        print(sql_templ % tuple(values))

# print_as_sql(data)









