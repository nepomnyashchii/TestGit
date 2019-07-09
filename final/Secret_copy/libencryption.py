from cryptography.fernet import Fernet

def read():
    with open('key.txt', 'r') as f:
        f_contents = f.read()
    key = f_contents
    data = Fernet(key)
    return data

def encrypt(msg):
    encryption =read()
    msgn =bytes(msg)
    encrypted_msg = encryption.encrypt(msgn)
    return encrypted_msg

def decrypt(msg):
    decryption = read()
    msgn = bytes(msg)
    decrypted_msg = decryption.decrypt(msgn)
    return decrypted_msg