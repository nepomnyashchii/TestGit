import logging
import os


def createLogFolder():
    path = "./logs"
    try:
        # raise OSError(2, 'Custom error message', 'asdasdasdasd asd as')
        if os.path.exists(path):
            print("Directory logs already exists")
        else:
            os.makedirs(path)
            print("Successfully created the directory logs")
    except OSError as error:
        print("Error in createLogFolder :%s " % error)


def setup_logger(loggerName):
    createLogFolder()
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    dh = logging.FileHandler('./logs/debug.log')
    dh.setLevel(logging.DEBUG)

    eh = logging.FileHandler('./logs/error.log')
    eh.setLevel(logging.ERROR)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    dh.setFormatter(formatter)
    eh.setFormatter(formatter)

    logger.addHandler(eh)
    logger.addHandler(dh)
    return logger


def getModuleLogger(moduleName):
    return logging.getLogger(moduleName)
