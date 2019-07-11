from cryptography.fernet import Fernet
import logger_module

logger = logger_module.setup_logger("secret-3libencryption")

def get_cryptor():
    logger.debug("Start to write a key to key.txt file")
    with open('key.txt', 'r') as f:
        f_contents = f.read()
    key = f_contents
    # logger.debug("Get a key: " + key)
    cryptography = Fernet(key)
    return cryptography

def encrypt(msg):
    logger.debug("Start encryption with a key")
    encryption = get_cryptor()
    msgn =bytes(msg)
    encrypted_msg = encryption.encrypt(msgn)
    logger.debug("Encrypted message: " + encrypted_msg)
    return encrypted_msg

def decrypt(msg):
    logger.debug("Start decryption")
    decryption = get_cryptor()
    msgn = bytes(msg)
    decrypted_msg = decryption.decrypt(msgn)
    logger.debug("Decrypted message: " + decrypted_msg)
    return decrypted_msg