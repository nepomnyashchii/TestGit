# def reverse_slicing(s):
#     return s[::-1]
# print(reverse_slicing("alec"))


def reverse_for_loop(s):
    s1 = ''
    for c in s:
        print(c)
        s1 = c + s1
        print(s1)  # appending chars in reverse order
    return s1


print(reverse_for_loop("alec"))
