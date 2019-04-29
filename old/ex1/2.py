
def by_by():
    print("bye bye")


def my_hello(name):
    print("Hello" + name)


def inc(num):
    return num+1


def many_params(a1, a2, a3):
    return a1+a2+a3


my_hello("Alec")
mynum = inc(3)
print(mynum)
print(many_params(1, 2, 3))
print(many_params("I am ", "cool ", "guy"))
by_by()
