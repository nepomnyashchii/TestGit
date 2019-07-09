from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(type(key))
print(key)