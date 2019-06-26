
# test = {'key' : 2,
# "keys": 3
# }
# name =test["key"]
# name1 =test["keys"]
# print(name)
# print(name1)

# test= {
#     'name' : "Alexander",
#     'lastname' : "Nepomnyashchii"
# }
# try:
#     name =test['name']
#     name =test['mama']
#     # keyerror (we have the key error which affects the results)
#     print(test)
# except KeyError:
#     print("There is no such key")

# test ={
#     125:3,
#     120:4
# }
# print(test[125])

# primes ={
# 1:2,
# 2:3,
# 4:7,
# 7:17
# }
# print(primes[primes[4]])

# test ={
#     "lake":3,
#     "music":4
# }
# if "lake" not in test:
#     print("Data Exist!")
# else:
#     print("No data in the dictionary")

# contacts = {
#     "Alexander Nepomnyashchii": 5677888888,
#     "Natasha Nepomnyashchaya": 44555555555
# }

# testing = input("Whom are we looking for: ?")
# if testing in contacts:
#     print("The contact is found" +contacts[testing])
# else:
#     print("Contact is not found")

# contacts ={
#     "Alexander Nepomnyashchii": 5677777777,
#     "Natasha Nepomnyashchaya" : 4566666666,
# }
# # print(contacts.get("Alexander Nepomnyashchii"))
# print(contacts.get("Maria Nepomnyashchaya", "The contact is not found"))

fib ={
    1:1,
    2:1,
    3:2,
    4:3
}
print(fib.get(4,0) + fib.get(7,5))






