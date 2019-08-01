
import mysql.connector
import logger_module

logger = logger_module.setup_logger("open_dblib")


def open_db():
    try:
        logger.debug('open_db function invoked')
        mydb = mysql.connector.connect(
            host="db4free.net",
            user="coolspammail",
            passwd="coolspammail-pass",
            database="coolspammail"
        )
        logger.debug('open_db finished')
        return mydb
    except mysql.connector.Error as error:
        logger.error('There is no DB connection: {}'.format(error))