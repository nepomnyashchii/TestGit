from cryptography.fernet import Fernet
key = 'IscdSPJ0zku3uRTU9vqVvjQ3ekbg4_xfDbxcK8VvQAg='
# data = Fernet(key)
# # encrypted_text = data.encrypt(b'SuperSecretpassword')
with open('1.txt', 'a') as f:
    f.write(key)