
def isAlphabet(x):
    return x.isalpha()

def reverse(string):
    LIST = toList(string)
    r = len(LIST) - 1
    l = 0
    while l < r:
        LIST[l], LIST[r] = swap(LIST[l],LIST[r])
        l += 1
        r -= 1
    return toString(LIST)

def toList(string):
    List = []
    for i in string:
        List.append(i)
    return List

def toString(List):
    return ''.join(List)

def swap(a, b):
    return b, a

# Driver
string = "sshshh*8888"
print ("Input string: ") + string
string = reverse(string)
print ("Output string: " + string)

