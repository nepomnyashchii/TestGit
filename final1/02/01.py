import lib
import datetime

msg = "privet"
exp = 600
pin = 1234
created = datetime.datetime(2019, 4, 25, 17, 10, 11)

sid = lib.put_secret(msg, pin, exp)
msg = lib.get_secret(sid, pin)
print(msg)

isEpx = lib.is_expired(created, exp)
print(isEpx)
