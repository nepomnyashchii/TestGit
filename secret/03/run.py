import lib

msg = "privet"
exp = 600
pin = 1234

sid = lib.put_secret(msg, pin, exp)
msg = lib.get_secret(sid, pin)
print(msg)
