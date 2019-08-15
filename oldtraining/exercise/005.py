# n = 10
# for i in range(n):
#     for j in range(i):
#         print('* ', end="")
#     print('')

# for i in range(n, 0, -1):
#     for j in range(i):
#         print('* ', end="")
#     print('')


# c++ style
# for(i=0;i<=n;i++){
#     for(i=0;i<=n;i++){
#         print()
#     }
#     print()
# }

def create_row(length):
    ac = ''
    for i in range(length):
        ac += '* '
    return ac + "\n"


n = 5
acamulator = ''

for i in range(n):
    acamulator += create_row(i)

for i in range(n, 0, -1):
    acamulator += create_row(i)

print(acamulator)


# n = 5
# acamulator = ''

# for i in range(n):
#     acamulator += '* ' * i + "\n"

# for i in range(n, 0, -1):
#     acamulator += '* ' * i + "\n"


# print(acamulator)
