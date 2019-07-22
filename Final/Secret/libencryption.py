from cryptography.fernet import Fernet
import logger_module
import os.path

logger = logger_module.setup_logger("libencryption")

def check_key ():
    try:
        if os.path.isfile('./key.txt'):
            return True
        else:
            return False
    except IOError:
        logger.error('An error occured trying to read the file.')
    except ValueError:
        logger.error('Non-numeric data found in the file.')
    except KeyboardInterrupt:
        logger.error('You cancelled the operation.')
    except Exception as ex:
        logger.error(ex)
    # else:
    #     # raise FileNotFoundError
    #     return {"File does not exist"}

def get_cryptor():
    try:
        logger.debug("Start to read a key")
        with open('key.txt', 'r') as f:
            f_contents = f.read()
        key = f_contents
        # logger.debug("Get a key: " + key)
        cryptography = Fernet(key)
        return cryptography
    except IOError:
        logger.error('An error occured trying to read the file.')
    except ValueError:
        logger.error('Non-numeric data found in the file.')
    except KeyboardInterrupt:
        logger.error('You cancelled the operation.')
    except Exception as ex:
        logger.error(ex)


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
    except Exception as ex:
        logger.error(ex)
    return encrypted_msg



def decrypt(msg):
    try:
        logger.debug("Start decryption")
        decryption = get_cryptor()
        msgn = bytes(msg)
        decrypted_msg = decryption.decrypt(msgn)
        logger.debug("Decrypted message: xxx")
    except IOError:
        logger.error('An error occured trying to read the file.')
    except ValueError:
        logger.error('Non-numeric data found in the file.')
    except KeyboardInterrupt:
        logger.error('You cancelled the operation.')
    except Exception as ex:
        logger.error(ex)
    return decrypted_msg

