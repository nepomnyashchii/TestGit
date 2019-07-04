"""Check what actions are possible in the directory list"""
print(dir(list))

list1 = ["orange", "apple", "peach"]

"""Obtain certain information from the list"""
data = list1[0]
print(type(data))
print(data)
"""Answer is orange: (element:str in this case) and not the element of the list"""

""" Take two parameters from the list"""

data = list1[0:1]
print(type(data))
print(data)
"""Answer is ["orange"] (element of the list) and not the element(string)"""

data = list1[0:2]
print(data)
""" Answer ["orange", "apple] ("the second element is not included)"""

"""Possible to skip the first number"""
data = list1[:2]
print(data)
""" Answer ["orange", "apple"] (the second element is not included)"""

"""The example with the number first in the list"""
data = list1[1:]
print(data)
""" Answer ["apple", "peach"] (the second element included in this case) """


""" Add data to the list"""

list1.append("grapes")
print(list1)
"""Answer ["orange", "apple", "peach", "grapes"]"""

""" Cannot do variable to the action; data  list.append("grapes")
print(data) will give responce none """

data = list1.count("grapes")
print(data)

""" Delete last parameter """
list1.pop()
print(list1)

"""Delete certain parameter"""
list1.pop(1)
print(list1)
"""We must use a number not a word"""

"""Delete the whole list python3 command(there is no such command in python2.7"""
list1.clear()
print(list1)

"""Create list from the tuple"""

data = list((1,2,3))
print(data)

""" Obtain from the list of tuples: two different parameters"""
data = [(0,2,3) ,(3,4,5)]
new_list = []
for element in data:
    data1 =element
    # print(data1)
    data =list(data1)
    # print(data)
    for element in data:
        data1 = element
        print(data1)
        new_list.append(data1)
        print(new_list)




# """Example how to obtain from list of tuples a list)"""
# list = (('1','a'),('2','b'),('3','c'),('4','d'))
# list1 = []
# list2 = []
# list3=[]
# for i in list:
#    list1.append(i[0])
#    list2.append(i[1])
#    list3.append(i)
# print(list1)
# print(list2)
# print(list3)







