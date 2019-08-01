from cryptography.fernet import Fernet
import logger_module
import os.path
import config

logger = logger_module.setup_logger("libencryption")

def check_config ():
    try:
        logger.debug("Check key")
        if os.path.isfile('./config.py'):
            return True
        else:
            return False
    except IOError:
        logger.error('An error occured trying to read the file.')
    except Exception as error:
        logger.error(error)


def get_cryptor():
    try:
        logger.debug("Start to read a key")
        key = config.key
        # logger.debug("Get a key: " + key)
        cryptography = Fernet(key)
    except IOError:
        logger.error('An error occured trying to read the file.')
    except Exception as error:
        logger.error(error)
    return cryptography

def encrypt(msg):
    try:
        logger.debug("Start encryption with a key")
        encryption = get_cryptor()
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

