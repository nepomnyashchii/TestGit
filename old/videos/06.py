# filename = input("Enter a file: ")
# file = open('test.txt', 'r')
# # file.read()
# # "w" is the regime to change the file information
# print(str(len(file.read())))

# file.close()

# file = open('test.txt', 'w')
# file.write("Hello World")
# file.close()

# filename = input("Enter wanted filename: ")
# text = input("Enter Text, which you want to put in a file: ")
# file = open(filename, 'w')
# file.write(text)

# file.close()

# file = open('test.txt', 'r')
# print(file.read(1))
# print(file.read(4))
# file.close()
# we can open certain amount of information
# "w" is the regime to change the file information
# print(str(len(file.read())))

# file = open('test.txt', 'a')
# print(file.write("test"))
# file.close()

# file =open('test.txt', 'r')
# for i in range (3):
#     print(file.read(2))
# file.close()

# filename1 =input("Enter name of the file: ")
# filename2 = input("Enter name of the second file")
# file1 = open(filename1, 'r')
# file2 = open(filename2, 'w')
# file2.write(file1.read())
# file1.close ()
# file2.close()

# print("Copy action is succesfully accomplished")

# filename1 = input("Enter name of the character: ")
# filename2 = "backup_" + filename1
# file1 = open(filename1, 'r')
# file2 = open(filename2, 'w')
# file2.write(file1.read())
# file1.close ()
# file2.close()

# filename1 = input("Enter name of the character: ")
# filename2 = "backup_" + filename1
# file1 = open(filename1, 'rb')
# file2 = open(filename2, 'wb')
# file2.write(file1.read())
# file1.close ()
# file2.close()
# print("Backup successfuly formed")


# file =open('test.txt', 'r')
# strings = file.readlines()
# print(strings)
# file.close()

# file = open('test.txt', 'r')
# strings = file.readlines()
# for string in strings:
#     print(string)
# file.close()

# with open('test.txt', 'r') as f:
#     # file is automatically closed
#     print(f.read())
# print("File is already finished")

with open('test.txt', 'r') as f:
    # file is automatically closed
    strings =f.readlines()
    for element in strings:
        print(element)
print("File is already finished")















