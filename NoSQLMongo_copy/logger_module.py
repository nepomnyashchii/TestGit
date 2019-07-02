import logging


def setup_logger(loggerName):
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
