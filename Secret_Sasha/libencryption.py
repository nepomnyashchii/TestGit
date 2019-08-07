from cryptography.fernet import Fernet
import logger_module
import os.path

key = ''
logger = logger_module.setup_logger("libencryption")


def set_key(my_key):
    global key
    key = my_key
    print("\n\n-------------\n\n\n")
    print(key)

def get_cryptor():
    global key
    try:
        logger.debug("Start to read a key")
        # logger.debug("Get a key: " + key)
        print("\n\n-------------\n\n\n")
        print(key)
        cryptography = Fernet(key)
        print("\n\n-------------\n\n\n")
        print(cryptography)
        print("\n\n-------------\n\n\n")
        return cryptography
    except IOError:
        logger.error('An error occured trying to read the file.')
    except Exception as error:
        logger.error(error)
    return None


def encrypt(msg):
    try:
        logger.debug("Start encryption with a key")
        print("\n\n-------------\n\n\n")
        encryption = get_cryptor()
        print(encryption)
        print("\n\n-------------\n\n\n")
        msgn = bytes(msg)
        encrypted_msg = encryption.encrypt(msgn)
        logger.debug("Encrypted message: " + encrypted_msg)
    except IOError:
        logger.error('An error occured trying to read the file.')
    except ValueError:
        logger.error('Non-numeric data found in the file.')
    except KeyboardInterrupt:
        logger.error('You cancelled the operation.')
    except Exception as error:
        logger.error(error)
    return encrypted_msg


def decrypt(msg):
    try:
        logger.debug("Start decryption")
        decryption = get_cryptor()
        msgn = bytes(msg)
        decrypted_msg = decryption.decrypt(msgn)
        logger.debug("Decrypted message: " + decrypted_msg)
    except IOError:
        logger.error('An error occured trying to read the file.')
    except ValueError:
        logger.error('Non-numeric data found in the file.')
    except KeyboardInterrupt:
        logger.error('You cancelled the operation.')
    except Exception as error:
        logger.error(error)
    return decrypted_msg
