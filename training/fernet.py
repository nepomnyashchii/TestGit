from cryptography.fernet import Fernet

def encrypt ():
    key = Fernet.generate_key()
    f = Fernet(key)
    apple = "success"
    result =bytes(apple)
    token = f.encrypt(apple)
    return decrypt(token)

result=encrypt()
print(result)

def decrypt (token):
    result2 =f.decrypt(token)
    print(result2)
    return result2
