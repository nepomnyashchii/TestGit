from flask import Flask, request, jsonify
import dblib
import logger_module
import libencryption


logger = logger_module.setup_logger("secret")
logger.debug('Start my super App')
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['APPLICATION_ROOT'] = '/api'
print("\n\n\n")


@app.route('/')
def index():
    logger.debug("Request for testing connection invoked")
    return 'Secret API is online :)'


@app.route('/ping')
def ping():
    logger.debug("Request for ping")
    return jsonify(data='pong'), 200


@app.route('/secret/put/<msg>/<int:pin>/<int:exp>', methods=['GET'])
def put(msg, pin, exp):
    encrypted_msg = libencryption.encrypt(msg)
    logger.debug("Invoke: put a get")
    sid = dblib.put_secret(encrypted_msg, pin, exp)
    logger.debug("Obtain sid: " + sid)
    return jsonify(sid=sid)


@app.route('/secret', methods=['POST'])
def post_secret():
    logger.debug("Invoke: put from a post")
    result = request.json
    msg = result["msg"]
    pin = result["pin"]
    exp = result["exp"]
    encrypted_msg = libencryption.encrypt(msg)
    sid = dblib.put_secret(encrypted_msg, pin, exp)
    return jsonify(sid=sid)


@app.route('/secret/<sid>/<int:pin>', methods=['GET'])
def get_secret(sid, pin):
    logger.debug("Obtain msg from the database")
    msg = dblib.get_secret(sid, pin)
    if len(msg) > 0:
        logger.debug("Message obtained: " + msg)
        decrypted_msg = libencryption.decrypt(msg)
        return jsonify(msg=decrypted_msg)
    else:
        return jsonify({
            'status': "404: request",
            'message': 'pin or sid is wrong: ' + request.url,
        })

@app.route('/get_secret', methods=['POST'])
def post_get_secret():
    logger.debug("Obtain msg from the database")
    result = request.json
    sid = result["sid"]
    pin = result["pin"]
    msg = dblib.get_secret(sid, pin)
    if len(msg) > 0:
        logger.debug("Message obtained: " + msg)
        decrypted_msg = libencryption.decrypt(msg)
        return jsonify(msg=decrypted_msg)
    else:
        return jsonify({
            'status': "404: request",
            'message': 'pin or sid is wrong: ' + request.url,
        })


@app.route('/secret/<sid>/<int:pin>', methods=['DELETE'])
def del_secret(sid, pin):
    logger.debug("Delete data from database")
    if len(sid) > 0:
        del_id = dblib.del_secret(sid, pin)
        logger.debug("Sid succesfully deleted: " + str(del_id))
    else:
        print("Sid does not exist")
    logger.debug('End my super App')
    return jsonify(deleted_sid=sid)


@app.errorhandler(404)
def not_found(error=None):
    logger.debug("Start app.errorhandler to confirm status 404")
    message = {
        'status': 404,
        'message': 'URL not found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
