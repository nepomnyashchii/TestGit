name = "Alex"
number = 3
print("Phone number of " + name + " is " + str(number))
# print("Phone number of %s is %s ---- %s" % (name, number, "asd"))

my_expence_list = [200, 334, 21, 19]
for number in my_expence_list:
    print(number)


phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
# for key, value in phonebook.items():
#     print("Phone number of " + key + " is " + str(value))


newname = input("Give me name: ")
if newname in phonebook:
    print(phonebook[newname])
else:
    print("Key not found")
