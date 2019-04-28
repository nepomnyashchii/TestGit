import lib
import datetime
import time
import uuid

msg = "success"
exp = 600
pin = 1234
sid = str(uuid.uuid4())
created=time.strftime('%Y-%m-%d %H:%M:%S')

# sid = lib.put_secret(msg, pin, exp, created)
# msg = lib.get_secret(sid, pin)
# print(msg)
# # lib.del_secret(sid, pin)

# print("Please wait...")
sid = lib.put_secret(msg, pin, exp, created)

if len(sid) > 0:
    print("Please wait...")
    msg = lib.get_secret(sid, pin)
    if len(msg) > 0:
        print(msg)
    else:
        print("secret not found in db")
else:
    print("cant put msg to db")
