import logger_module
import os

logger = logger_module.setup_logger("utils")


def check_config():
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
