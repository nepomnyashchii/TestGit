# def compare (value_1, value_2):
#     if value_1 == value_2:
#         return "Yes"
#     else:
#         return "No"
# print(compare(3,3))

# def compare(value_1, value_2, value_3):
#     if value_1== value_3 and value_2==value_3:
#         return "Yes"
#     else:
#         return "No"
# print (compare(1,1,1))


# def compare (values):
#     x = range(10)
#     for l in x:
#         if values==l: 
#             return "Yes"
#     else:
#         return "No"
# print (compare(20))


# def compare(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
#     if x2==x1 and x3==x1 and x4==x1 and x5==x1 and x6==x1 and x7==x1 and x8==x1 and x9==x1 and x10==x1:
#         return "Yes"
#     else:
#         return "No"
# print compare(1,1,1,1,1,1,1,1,1,1)





# def compare(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
#     if x2==x1 and x3==x1 and x4==x1 and x5==x1 and x6==x1 and x7==x1 and x8==x1 and x9==x1 and x10==x1 or x2 == None:
#         return "Yes"
#     else:
#         return "No"
# print (compare(1,1,1,1,1,1,1,1,1,1))




# def compare(*args):
#     for element in args:
#         x1 = args[0]
#         x2 = args[1]
#         x3 = args[2]
#         x4 = args[3]
#         x5 = args[4]
#         x6 = args[5]
#         x7 = args[6]
#         x8 = args[7]
#         x9 = args[8]
#         x10 = args[9]
#         if x2==x1 and x3==x1 and x4==x1 and x5==x1 and x6==x1 and x7==x1 and x8==x1 and x9==x1 and x10==x1:
#             return "Yes"
#     else:
#         return "No"
# print (compare(1,1,1,1,1,1,1,1,1,1))

# def compare(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
#     if x2==x1 and x3==x1 and x4==x1 and x5==x1 and x6==x1 and x7==x1 and x8==x1 and x9==x1 and x10==x1 or x2 == None:
#         return "Yes"
#     else:
#         return "No"
# print (compare(1,1,1,1,1,1,1,1,1,1))


# def myFun(*argv):
#     data = []
#     for arg in argv:
#         result = data.append(arg)
#     return data
# data =myFun(1,1,1,1,1)
# result = len(data)
# print("Number of parameters: " + str(result))
# text = ''
# for element in data:
#     if data[0]== element:
#         text += element
#     else:
#         print("No")


# def myFun(*argv):
#     data = []
#     for arg in argv:
#         result = data.append(arg)
#     return data
# data =myFun(1,1,1,1,1)
# result = len(data)
# print("Number of parameters: " + str(result))



# def myFun(*argv):
#     for arg in argv:
#         if argv[0] == arg:
#             data = len(argv)
#             print ("Yes")
#         else:
#             print ("No")
# print(myFun(2,1,2))


# def myFun(*argv):
#     text = []
#     for arg in argv:
#         if argv[0] == arg:
#             data = len(argv)
#             text += str(arg)
#             print("Yes")
#         else:
#             print ("No")
#     return text
# print(myFun(1,2,2))

# def myFun(*argv):
#     data = []
#     for arg in argv:
#         result = data.append(arg)
#     return data
# data =myFun(1,1,1,1,1)
# result = len(data)
# print("Number of parameters: " + str(result))


# def myFun(*argv):
#     data = []
#     value = " "
#     for arg in argv:
#         result = data.append(arg)
#     print(data)
#     if data[0]==data[1]==data[2]:
#         return "Yes"
#     else:
#         return "No"
# data = myFun(1,1,1)
# print(data)


# def myFun(*argv):
#     data = []
#     value = " "
#     for arg in argv:
#         result = data.append(arg)
#     print(data)
#     if data.count(data[0]) == len(data):
#         return "Yes"
#     else:
#         return "No"
# data = myFun(1,1,1)
# print(data)



#     if data[0] ==data[1] and data[0]==data[2] and data[0] == data[3]:
#         print(value) = "Yes"
#         return value
#     return value
# value =myFun(1,5,1,1,1)
# print(value)



# def data(parameters1, parameters2, parameters3, parameter4, parameters5):
#     data = [0,1,2,3,4]
#     if data[0]== data[1]== data[2]== data[3] ==data[4]:
#         return "Yes"
#     else:
#         return "No"
# data = data (0,1,2,3,4)
# print(data)


# def myFun(*argv):
#     data = []
#     value = " "
#     for arg in argv:
#         result = data.append(arg)
#     print(data)
#     if data.count(data[0]) == len(data):
#         return "Yes"
#     else:
#         return "No"
# data = myFun(1,1,1)
# print(data)


# def myFun(*argv):
#     if argv.count(argv[0]) == len(argv):
#         return "Yes"
#     else:
#         return "No"
# print(myFun(1,2,1))


def myFun(*argv):
    for arg in argv:
        if arg!=argv[0]:
            return "No"
    else:
        return ("Yes")
print(myFun(1,1,3,1))



# data = [9,10,10]
# if data[0]!=data[1]:
#     print("Yes")



