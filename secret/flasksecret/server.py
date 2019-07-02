from flask import Flask
import lib
import logger_module


logger = logger_module.setup_logger("secret")
logger.debug('Start my super App')
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
print("\n\n\n")

@app.route('/')
def index():
    logger.debug("Request for testing connection invoked")
    return 'Secret Runner :)'
# get data through todo (not forget to transfer obtained tuple to the string)


@app.route('/put/<msg>/<int:pin>/<int:exp>')
def put(msg, pin, exp):
    return lib.put_secret(msg, pin, exp)


@app.route('/get/<sid>/<int:pin>')
def get(sid, pin):
    msg = lib.get_secret(sid, pin)
    if len(msg) > 0:
        return '{ "msg": "' + msg + '"}'
    else:
        return '{"error":"not found"}'
