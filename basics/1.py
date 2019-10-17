# array=['a','b','b','a', 'c']

# def reverse(s):
#     return s[::-1]

# print(reverse("money"))

# string='abr1rba'

# rs=string[::-1]
# print(rs)


# if string == rs:
#     print('polindrom')
# else:
#     print('not polindrom')


# def isPalindrome(str):

#     # Run loop from 0 to len/2
#     for i in xrange(0, len(str)/2):
#         if str[i] != str[len(str)-i-1]:
#             return False
#     return True


# tmp=array[0]
# array[0]=array[1]
# array[1]=tmp
# print(array)


# for e in array:
#     print(e)

# tmp=array[0]
# array[0]=array[-1]
# array[-1]=tmp

# for e in array:
#     print(e)


# array[array.len()-1]


# str="abcdefghij"
# for i in range(1,len(str)/2):
#     print(str[-i])

# def myIsPolyndrom(str):
#     for index in range(0,len(str)/2):
#         bindex= len(str)-index-1
#         if str[index] != str[bindex]:
#              return False
#     return True


# print(myIsPolyndrom('asssa'))


# def my_reverse_short_version(my_str):
#     ls = list(my_str)
#     for i in xrange(0, len(ls)/2):
#         bi = len(ls)-i-1
#         ls[i], ls[bi] = ls[bi], ls[i]
#     return "".join(ls)


# def my_reverse(my_str):
#     ls = list(my_str)
#     for i in xrange(0, len(ls)/2):
#         bi = len(ls)-i-1
#         tmp = ls[i]
#         ls[i] = ls[bi]
#         ls[bi] = tmp
#     return "".join(ls)


# print(my_reverse('abc1d'))
# print(my_reverse_short_version('abc1d'))


# def char_count(my_char, my_str):
#     count = 0
#     for e in my_str:
#         if e == my_char:
#             count += 1
#     return count


# # print(char_count("a", "jopajopasajopa"))


# a = ['a', 1, [1, 3, "s"]]
# print(a)
# a[0], a[2][-1] = a[2][-1], a[0]
# print(a)

a = "alec"
b = list(a)
print(b)
b[1], b[0] = b[0], b[1]
print(b)
c ="".join(b)
print(c)