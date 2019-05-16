import lib
import datetime
import time
import uuid
import logging
logger = lib.setup_logger()
logger.debug('Start my super App')

msg = "success"
exp = 60000
pin = 1234


# logger.error('Some error')

# lib.del_secret(sid, pin)

print("Please wait...")
logger.debug(
    'Testing put_secret() with msg= {}   exp = {}   pin = {} '.format(msg, exp, pin))

sid = lib.put_secret(msg, pin, exp)
logger.debug(' put_secret() returned sid = {} '.format(sid))

if len(sid) > 0:
    print("Please wait...")
    logger.debug('lib.get_secret with  sid = {}   pin= {}'.format(sid, pin))
    msg = lib.get_secret(sid, pin)
    logger.debug(' get_secret returned msg  = {}'.format(msg))
    if len(msg) > 0:
        logger.debug('app succesdd')
        print(msg)
    else:
        logger.debug('secret not found or expired')
        print("secret not found or expired")
else:
    logger.error('len(sid) <= 0')
    print("cant put msg to db")


logger.debug('End my super App')
