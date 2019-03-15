def say_hi(name, age):
    print("Hello " + name + " you are " + age)


say_hi("Mike", "35")
say_hi("Steve", "70")


def my_team(Spain, England, Russia):
    print("My favourite team is " + Spain + England + Russia)


my_team("Barcelona", "Real", "Juventus")
my_team("Cska", "Spartak", "Dynamo")
my_team("Zenit", "Milan", "Lokomotiv")


def my_music(Shopen, Mozart, Bach):
    print("My favourite composers are " +
          Bach + " " + Shopen + " and " + Mozart)


my_music("Rasputina", "Allegrova", "Pugacheva")


def my_cube(num):
    return num*num*num


print(my_cube(3))


def my_division(num1, num2):
    return num1-num2


print(my_division(30, 23))


def raise_to_power(base_num, pow_num):
    result = 1
    for element in range(pow_num):
        result = result*base_num
    return result


print(raise_to_power(3, 4))
