from cryptography.fernet import Fernet
key = 'IscdSPJ0zku3uRTU9vqVvjQ3ekbg4_xfDbxcK8VvQAg='
data = Fernet(key)
encrypted_text = 'gAAAAABdJN6JRGqn7f_rBSZAyZc9Op4onCCZpB4jzwjjj4oNVltyHhmI6UBAELgIyuHu1pGE6ckpzAnZzdz0gKmehu522ousWlrm8J6YB2c88yw90cMmwb0='
decrypted_text = (data.decrypt(encrypted_text))
print(decrypted_text)