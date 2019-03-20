#example with return
def calculate_sum (expence):
    total=0
    for number in expence:
        total=total +number
    return total

my_expence_list = [200, 334, 21,19]
sasha_expence_list=[20,500,700]
levy_expence_list=[56,34,28,45,67]
my_total=calculate_sum(my_expence_list)
sasha_total=calculate_sum(sasha_expence_list)
levy_total= calculate_sum(levy_expence_list)
print("My total expenses", my_total)
print ("Sasha's total expenses", sasha_total)
print("Levy's total expenses", levy_total)


# without returning function
# def my_name(name):
#     print("My name is:" , name)
# my_name("Alec")
# my_name("Joe")
#
# #several arguments
# def my_biography(name, gender, age, height):
#
#     print ("Name: ", name)
#     print ("Gender: ", gender)
#     print("Age", age)
#     print("Height", height)

# my_biography("Alec", "male", 39, "1.73 cm")
# my_biography("Sasha", "male", 40, "1.75 cm")

def f(a, List=[]):
    List.append(a)
    return List

print(f(1))
print(f(2))
print(f(5))
print(f(10))


