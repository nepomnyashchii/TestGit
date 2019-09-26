
def Listconversion(string):
    List = []
    for i in string:
        List.append(i)
    return List


def reverse(string):
    LIST =Listconversion(string)
    r = len(LIST) - 1
    l = 0
    while l < r:
        LIST[l], LIST[r] = swap(LIST[l],LIST[r])
        l += 1
        r -= 1
    return toString(LIST)

def swap(a, b):
    return b, a

def toString(List):
    return ''.join(List)


string = "papai"
print ("Input string: ") + string
string = reverse(string)
print ("Output string: " + string)

