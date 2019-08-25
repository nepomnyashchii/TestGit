my_string = "python"
x = 0
for i in my_string:
    x+= x
    print(my_string[0:x])
    
def reverse_for_loop(s):
    s1 = ''
    for c in s:
        print(c)
        s1 = c + s1
        print(s1)  # appending chars in reverse order
    return s1