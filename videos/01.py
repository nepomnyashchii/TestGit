print("Hello \nWorld") # next line
print("Hello \"World\"") # arrange signs
print('''Hello
mama
World''')     # arrange certain data
print('''Hello
World''')     # arrange other data
# 2test mistake

# a =input("Enter the first number:")
# b = input("Enter the second number:")
print(2+2)
print("2" +"2")
print("Hello "*3)
# print("Hello"*4.0)
test =10
# del(test)
print(test)
test = 10
test +=10
print(test)
test =10
test =11
print(test)
print(10==11)
print(11==11)
print(12==12)
print(10==13)
print(5>=5)
print(5<=5)
print(7>7.0)
print("test">"tesa")  # each word has its weight ("We can compare weight of the words")
print("aaa" > "bbb")
weather = "winter"
print("program started")
if weather == "winter":
    print("Now the weather is bad")
    print("aaa")
print("Program is finished")

weather = "summer"
print("Program started")
if weather == "winter":
    print("Now the weather is bad")
    print("aaa")
print("Program is finished")

weather ="summer"
time ="night"
print("Program started")
if weather == "summer":
    if time == "night":
        print("I love summer's night")
print ("Program is done")

weather = "summer"
time = "morning"
print("Program started")
if weather == "summer":
    print("Everything is ok")
    if time =="evening":
        print("I am at home")
    if time == "morning":
        print("I love to go to work")

# weather = "summer"
# time = "morning"
# print("Program started")
# if weather == "winter":
#     print("Everything is ok")
# else:
#     print("The day was bad")

weather = "fall"
time = "morning"
print("Program started")
if weather == "winter":
    print("Everything is bad")
elif weather == "summer":
    print("Everything is ok")
elif weather == "spring":
    print("The summer is coming")
else:
    print ("The Fall is My Favourite Season")

weather = "fall"
if not weather == "summer":
    print("Everything is ok")

# i =1
# while i<=5:
#     print(i)
#     i+=1

# i =3
# while i<=3:
#     print(i)
#     i-=1

# i=1
# while 1 ==1:
#     print("Hello", i)
#     i+=1

#     if i==10:
#         break
# print ("Program Finished")

i =0
while i<=100:
    i=i+1
    if (i % 2)!= 2:
        continue
print("Even number " +str(i))

test = [1, 2, 3, [4, 5, 6]]
print(test[0])
print(test[3][1])

test =[0, 1, 2]
print(test * 2)
print(test + [0, 1, 2])

test = "Hello"
print(test[1])

print(test[4])

test = ["Alexander Nepomnyashchii", "Liliana Gusinskaya", "Lubov Cantor"]
if "Alexander Nepomnyashchii" in test:
    print("Alexander Nepomnyashchii is in text")
if "Mara Gutshabash" not in test:
    print("Mara Gutshabash is not in text")

test = []
test.append("Hello")
test.append([1,2,3])
print(test)

test = [1,2,3,4,5,6]
test.append(5)
test.remove(3)
test.insert(0,0)
test.insert(1,0)
print(test)
print("In the massive there are " + str(len(test)) + " elements")

test = [1,2,3,1,1,1]
test.reverse()
print(test)
print (max(test))
print(min(test))
print(test.count(1))
print(test.count(2))

test =5
print(list(range(test)))

print(list(range(5,10)))

print(list(range(5,11,2)))

numbers = range (5, 15, 3)
print(numbers[3])

numbers = [1,2,3,4,5]
i=0
length = len(numbers)-1
while i<=length:
    print(str(numbers[i]) + "!")
    i+=1

numbers = [3,4,5,6,7]
for i in numbers:
    print(str(i) + "!")

for test in range(3):
    print("Hello")

list = [1,1,2,3,5,8,13]
print(list[list[4]])

def print_spam ():
    print('spam')
    print('spam')
    print('spam')
print_spam()

# def max(x,y):
#     if x >y:
#         return x
#     else:
#         return y
#     print('test')
# x = float(input("Enter number 1: "))
# y =float(input("Enter number 2: "))
# print(max(x,y))

def howdy_ho ():
    '''function description'''
    print('howdy_ho')
print(howdy_ho.__doc__)

def my_day ():
    '''today is Sunday'''
print(my_day.__doc__)


def howdy_ho ():
    print("It is Tuesday")
var = howdy_ho
var ()

def my_day ():
    print("It is Tuesday")
night = my_day
night()

def shout(word):
    return word + "!"
speak = shout
output =speak('shout')
print(output)

# def howdy_ho (name):
#     print ("howdy_ho " + name + "!")

# def read_name ():
#     return ":::" + input("Enter your name:") + ":::"

# howdy_ho("abraham")

# def howdy_ho (namer):
#     print ("howdy_ho " + namer + "!")

# def read_namer (read):
#     return ":::" + input("Enter your name:") + ":::"
# howdy_ho("abraham")

def howdy_ho (name):
    print ("howdy_ho " + name + "!")

def read_name ():
    return ':::' + input("Enter your name: ") + ':::'
howdy_ho(read_name ())


def howdy_ho (name):
    print ("howdy_ho " + name () + "!")

def read_name ():
    return ':::' + input("Enter your name: ") + ':::'
howdy_ho(read_name)











































