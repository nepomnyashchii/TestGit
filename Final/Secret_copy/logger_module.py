import logging
import os

# define the name of the directory to be created


def createLogFolder():
    # path = "./logs"
    try:
        if not os.path.exists('./logs'):
            print("Data already exists")
    except os.makedirs('./logs'):
        print("Successfully created the directory")
    # else:
    #     print("Successfully created the directory %s " % path)
    # "

    # try:
    #     os.mkdir(path)
    # except OSError:
    #     print("Creation of the directory %s failed because it was already created" % path)



def setup_logger(loggerName):
    createLogFolder()
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    dh = logging.FileHandler('logs/debug.log')
    dh.setLevel(logging.DEBUG)

    eh = logging.FileHandler('logs/error.log')
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
