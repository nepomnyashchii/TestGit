from cryptography.fernet import Fernet
key = b'DFCr88GbnVuOn4AB2W34UJpzSu6NX14ekxesdg59us0='
cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(b"SuperSecretPassword")   #required to be bytes
print(ciphered_text)