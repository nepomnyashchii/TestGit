
# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print("I sleep all night and I work all day.")
#
# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
#
# def exp_1 ():
#     repeat_lyrics()
# exp_1 ()

# def hello_func ():
#     pass
# print(hello_func())
# print(hello_func)


# def hello_func ():
#     print("Hello Function?")
# hello_func()
# hello_func()
# hello_func()
# hello_func()

# def hello_func ():
#     print("Hello Function?")
# hello_func()
# hello_func()
# hello_func()
# hello_func()

# def hello_func ():
#     return("Hello Function?")
# print(hello_func())

# def hello_func ():
#     return("Hello Function?")
# print(hello_func().upper())

# def hello_func (greeting):
#     return("{} Function".format (greeting))
# print(hello_func("Hi Friend"))

# def hello_func (greeting, name="you"):
#     return("{}, {}".format (greeting, name))
# print(hello_func("Hi Friend"))

# def hello_func (greeting, name="you"):
#     return("{}, {}".format (greeting, name))
# print(hello_func("Hi Friend", name = "Jack"))

# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# def is_leap (year):
#     return year %4 ==0 and (year % 100!=0 or year % 400 ==0)
# def days_in_month(year,month):
#     if  1<=month<=13:
#         return "Year is good!"
#     if month==2 and is_leap(year):
#         return 29
#     return month_days(month)
# # print(is_leap(2016))
# print(days_in_month(2017,2))

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap (year):
    return year %4 ==0 and (year % 100!=0 or year % 400 ==0)
def days_in_month(year,month):
    if not 1<=month<=13:
        return "Invalid Month"
    if month==2 and is_leap(year):
        return 29
    return month_days[month]
# print(is_leap(2016))
print(days_in_month(2020,2))