import lib

msg = "jop1a"
exp = 600
pin = 1234
sid = "5d025a4c-5991-457d-a8f9-3e27de288b19"


lib.del_secret(sid, pin)
sid = lib.put_secret(msg, pin, exp)
msg = lib.get_secret(sid, pin)
print(msg)

print("Please wait...")
sid = lib.put_secret(msg, pin, exp)

if len(sid) > 0:
    print("Please wait...")
    msg = lib.get_secret(sid, pin)
    if len(msg) > 0:
        print(msg)
    else:
        print("secret not found in db")
else:
#     print("cant put msg to db")