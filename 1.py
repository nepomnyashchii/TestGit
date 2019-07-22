import sys
def name ():
    name= input("Enter: What is your name: ")
    my_name = "Your name is " + name + "\n"
    print(name)

def age ():
    age = input("Enter: What is your age: ")
    my_age = "You are " + age + " years old" + "\n"
    print(age)

def car():
    car = input ("Enter: what model is your car: ")
    my_car = "My model is: " + car + "\n"
    print(my_car)
    if my_car == "Mercedes":
        return my_car
    else:
        sys.exit("Wrong model")


# def car_model():
#     if car =="Mercedes":
#         car()
    # else:
    #     sys.exit("Wrong Model")
name()
age()
car()

# if car == "Mercedes":
#     "Everything is good"  
# else:
#     sys.exit("Wrong model")


