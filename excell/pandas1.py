import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


def print_as_table(df):
    for lineIndex in df.index:
        line_str = str(lineIndex) + ":\t"
        for columnName in df.columns:
            if columnName != 'OrderDate':
                line_str += columnName + "=" + \
                    str(df[columnName][lineIndex]) + "\t"
        print(line_str + "\n")


def print_as_csv(df):
    first_line = ""
    for columnName in df.columns:
        first_line += columnName + ","
    print(first_line)

    for lineIndex in df.index:
        line_str = ""
        for columnName in df.columns:
            line_str += str(df[columnName][lineIndex]) + ","
        print(line_str[:-1])


df = pd.read_excel('./data.xlsx', sheet_name='SalesOrders')
# print_as_table(df)
print_as_csv(df)

