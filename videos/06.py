filename = input("Enter a file: ")
file = open('test.txt', 'r')
file.write()
# "w" is the regime to change the file information
print(str(len(file.read())))

file.close()

