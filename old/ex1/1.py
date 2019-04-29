

def my_printline(myline):
    for c in myline:
        print(c)


def do_work():
    with open('1.txt', 'r') as f:
        for l in f:
            my_printline(l)


do_work()
