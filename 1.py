import sys

def name ():
    name= input("Enter: What is your name: ")
    my_name = "Your name is " + name + "\n"
    return age()

def age ():
    age = input("Enter: What is your age: ")
    my_age = "You are " + age + " years old" + "\n"
    print(my_age)
    if int(age)> 16:
        return car()
    else:
        sys.exit("You are too young")

def car():
    car = input ("Enter: what model is your car: ")
    my_car = car
    print(my_car)
    if my_car == "Mercedes":
        print("It is my car")
    else:
        sys.exit("You are in a wrong car")
        return my_car

name()





