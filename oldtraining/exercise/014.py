data = []
for i in range(100, 401):
    s = str(i)
    print(s)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        data.append(s)
# print(data)
l = ",".join(data)
print(l)
