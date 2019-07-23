import sys

def name ():
    name= input("Enter: What is your name: ")
    my_name = "Your name is " + name + "\n"
    print(my_name)
    return name

def age ():
    age = input("Enter: What is your age: ")
    my_age = "You are " + age + " years old" + "\n"
    print(my_age)
    return age

def car():
    car = input ("Enter: What model is your car: ")
    my_car = car
    print(my_car)
    return my_car

name()
age = age()

if int(age)> 16:
    my_car=car()
else:
    sys.exit("You are too young")

if my_car == "Mercedes":
    print("It is my car")
else:
     sys.exit("You are in a wrong car")


