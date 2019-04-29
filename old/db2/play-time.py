import datetime
import time


# a = datetime.datetime(100,1,1,11,34,59)
# b = a + datetime.timedelta(0,600) # days, seconds, then other fields.

# print a.time()
# print b.time()



dbtime=datetime.datetime(2019, 4, 23, 21, 32, 23)
print("dbtime")
print(dbtime)

exp=600

newtime = dbtime + datetime.timedelta(0,exp)
print("newtime")
print(newtime)

current_time = datetime.datetime.now()
# time.strftime('%Y-%m-%d %H:%M:%S')
print("current_time")
print(current_time)
print("\n\n")

if newtime > current_time:
    print("ok")
else:
    print("expired")

