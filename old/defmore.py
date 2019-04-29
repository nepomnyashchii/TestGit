# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print("I sleep all night and I work all day.")

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()

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

def hello_func (greeting, name="you"):
    return("{}, {}".format (greeting, name))
print(hello_func("Hi Friend"))

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

# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# def is_leap (year):
#     return year %4 ==0 and (year % 100!=0 or year % 400 ==0)
# def days_in_month(year,month):
#     if not 1<=month<=13:
#         return "Invalid Month"
#     if month==2 and is_leap(year):
#         return 29
#     return month_days[month]
# # print(is_leap(2016))
# print(days_in_month(2020,2))

# x=3
# def func (y):
#     print(y)
# func (x)


# x=3
# def func (x):
#     print(x)
# func (5)


# x = [1,2,3]
# def func (x):
#     x[1]=42
# func(x)
# print(x)
#
# x = [1,2,3]
# def func(x):
#     x[1]=42
#     x = "something else"
# func(x)
# print(x)

# def func(a, b,c):
#     print(a,b,c)
# func(1,2,3)

# def func (a,b,c):
#     print(a,b,c)
# func(a=1, c=2, b =3)

# def func(a, b=4, c=9):
#     print(a, b, c)
# func(1)
# func(7,5,9)
# func(42, c=9)
# func(42,43,44)

# def minimum (*n):
#     # print(type(n))
#     if n:
#         mn = n[0]
#         for value in n[1:]:
#             if value < mn:
#                 mn =value
#         print (mn)
# minimum (1, -3, 10, 20)
# minimum()

# values = [1, 3, -7, 9]
# def func(*args):
#     print(args)
# func(values)
# func(*values)

# def func(**kwargs):
#     print(kwargs)
# func(a=1, b=42)
# func(**{'a': 1, 'b' : 42})
# func(**dict(a=1, b=42))

# def connect(**options):
#     conn_params = {
#         "host": options.get("host", "127.0.0.1"),
#         "port": options.get('port', 5432),
#         "user": options.get("user", ''),
#         "pwd": options.get ("pwd", ""),}
#     print (conn_params)
# connect ()
# connect(host ="127.0.0.42", port=5433)
# connect(port=5431, user = "fab", pwd="gandalf")

# def func(a,b, c=7, *args, **kwargs):
#     print('a,b,c:', a, b, c)
#     print("args:", args)
#     print("kwargs:", kwargs)
# func (1, 2, 3, *(5,7,9), **{"A": 'a', "B": "b"})
# func (1,2,3, 5, 7, 9, A="a", B="b")

# def additional(*args, **kwargs):
#     print(args)
#     print(kwargs)
# args1 = (1,2,3)
# args2 = (4,5)
# kwargs1 = dict (option1=10, option2=20)
# kwargs2={"option3":30}
# additional(*args1, *args2, **kwargs1, **kwargs2)

# def func(a=[], b= []):
#     print(a)
#     print(b)
#     print("#"*12)
#     a.append(len(a))
#     b[len()]=len[a]

# def func(a=[], b= {}):
#     print(a)
#     print(b)
#     print('#'*12)
#     a.append(len(a))
#     b[len(a)]=len(a)
# func()
# func()
# func()