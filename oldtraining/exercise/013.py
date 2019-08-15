s = input("Input a string")
digits=strings=0
for c in s:
    if c.isdigit():
        digits+=1
    elif c.isalpha():
        strings+=1
print("Letters", digits)
print("Digits", strings)