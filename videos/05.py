# # exceptions are mistakes
# #control of the errors
# ImportError
# # (import of unknown library)
# IndexError
# # (number is not known as an example: you call number 5 and there are only 4 numbers in the table)
# NameError
# # (the argument does not exist)
# SyntaxError
# # ()
# TypeError
# # try to give some argument which is not connected with the information
# ValueError
# #

# print(test)
# print("2" + 4)
# list = [1,2,3,4,5]
# print(list[5])

# try:
#     print(7/0)
# except:
#     ZeroDivisionError
#     print("Divison for zero accepted")
# print ("Program is finished")
# try:
#     print(7/0)
# except:
#     pass
# print ("Program is finished")

# try:
#     eval('print(7/4)a')
# except ZeroDivisionError:
#     print("Division for zero accepted")
# except SyntaxError:
#     print("the day is long")
# print("Program is finished")

# try:
#     print(7/0)
# except ImportError:
#     print("the day is long")
# except ZeroDivisionError:
#     print("Division for zero accepted")
# except: SyntaxError
# print("Program is finished")

# special way to collect syntax error
# try:
#     eval('print(7/4)a')
# except ImportError:
#     print("the day is long")
# except ZeroDivisionError:
#     print("Division for zero accepted")
# except SyntaxError:
#     print("Today is morning")
# finally:
#     print("End of Catch of Errors")
# print("Program is finished")

# try:
#     weather ="winter"
#     if weather == "winter":
#         raise TypeError
# # raise certain errors (we need to find certain type of errors in sentences)
# except TypeError:
#     print("we obtained TypeError")

# try:
#     print(7/0)
# except:
#     print("test")
#     raise

# class HowdyHoError(Exception):
#     pass
# raise HowdyHoError ("Test")

# def exc(text):
#     assert text !=''
#     print(str(text) + "!")
# # exc('Hello World')
# exc('')

def test(number):
    assert number >0, "Number should be bigger than 0"
    print(number)
test (-10)






























