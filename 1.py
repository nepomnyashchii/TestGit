import sys

def name ():
    name= input("Enter: What is your name: ")
    my_name = "Your name is " + name + "\n"
    return age(age)

def age (age):
    age = input("Enter: What is your age: ")
    my_age = "You are " + age + " years old" + "\n"
    print(my_age)
    return check_age_limit(age)

def check_age_limit(age):
    if int(age)> 16:
        return car(car)
    else:
        sys.exit("You are too young")

def car(my_car):
    car = input ("Enter: what model is your car: ")
    my_car = car
    print(my_car)
    return check_my_car(my_car)

def check_my_car(my_car):
    if my_car == "Mercedes":
        print("It is my car")
        return("It is my car")
    else:
        sys.exit("You are in a wrong car")
name()


