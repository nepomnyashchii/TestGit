import logger_module
import os
import json


logger = logger_module.setup_logger("utils")


def check_config():
    try:
        logger.debug("check_config invoked")
        if os.path.isfile('./config.json'):
            return True
        else:
            return False
    except IOError:
        logger.error('An error occured trying to read the key.')
    except Exception as error:
        logger.error(error)


def get_config():
    try:
        logger.debug("get_config invoked")
        with open('./config.json') as json_file:
            data = json.load(json_file)
    except IOError:
        logger.error('An error occured trying to read the key.')
    except Exception as error:
        logger.error(error)
    return data
