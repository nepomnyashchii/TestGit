import pymongo
import dns
import requests
import json
import logger_module
import config

logger = logger_module.getModuleLogger('flowsapp.MYLIB')


def get_flowdata(user_name, user_flow):
    logger.debug("get_flowdata invoked with:" + user_name + " " + user_flow)
    """get flowdata from db."""
    logger.debug("Mongodb invoked")
    client = pymongo.MongoClient(config.MongoClient)
    db = client["test"]
    logger.debug("Connection with required collection invoked")
    mycol = db["flows"]
    myquery = {"name": user_name}
    mydoc = mycol.find(myquery)
    logger.debug("My query" + str(mydoc))
    data = mydoc[0]
    logger.debug("Query data from the database: " + str(data))
    flows = data["flows"]
    logger.debug("Queery data for flows" + str(flows))
    for flow in flows:
        if flow.get(user_flow):
            myresult = flow.get(user_flow)
        logger.error('An error occured.')
    logger.debug("get_flowdata finished with:" + str(myresult))
    return myresult


