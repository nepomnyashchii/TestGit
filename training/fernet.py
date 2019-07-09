from cryptography.fernet import Fernet

def encrypt ():
    key = Fernet.generate_key()
    f = Fernet(key)
    apple = "success"
    result =bytes(apple)
    token = f.encrypt(result)
    return token

result = encrypt()
print(result)



# result=encrypt()
# print(result)
# print(result)

def decryptencryp ():
    key = Fernet.generate_key()
    f = Fernet(key)
    apple = "lake"
    result =bytes(apple)
    token = f.encrypt(result)
    result2 = f.decrypt(token)
    return result2
print(decryptencryp())

