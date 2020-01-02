import libencryption


message = b'encrypt me!'

encrypted_msg = libencryption.encrypt(message)

print(encrypted_msg)
    
decrypted_msg = libencryption.decrypt(encrypted_msg)

print(decrypted_msg)
    


