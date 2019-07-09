from cryptography.fernet import Fernet
from cryptography.fernet import Fernet
key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
# data = Fernet(key)
# # encrypted_text = data.encrypt(b'SuperSecretpassword')
with open('1.txt', 'w') as f:
    f.write(key)