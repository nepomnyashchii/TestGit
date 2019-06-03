from flask import Flask
from flask import jsonify
from flask import request
import logging
app = Flask(__name__)

file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.ERROR)

@app.route('/', methods = ['GET'])
def api_hello():
    app.logger.info('informing')
    app.logger.warning('warning')
    app.logger.debug('DEBUG')
    app.logger.error('screaming bloody murder!')

    return "check your logs\n"
