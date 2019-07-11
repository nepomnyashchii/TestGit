from flask import Flask, request, jsonify
import lib
import logger_module
import libencryption


logger = logger_module.setup_logger("secret")
logger.debug('Start my super App')
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
print("\n\n\n")

@app.route('/')
def index():
    logger.debug("Request for testing connection invoked")
    return 'Secret Runner :)'

@app.route('/put/<msg>/<int:pin>/<int:exp>', methods =['GET'])
def put(msg, pin, exp):
    logger.debug("Start encryption")
    encrypted_msg = libencryption.encrypt(msg)
    logger.debug("Finished encryption: " + encrypted_msg)
    logger.debug("Start app to put data into the database")
    sid = lib.put_secret(encrypted_msg, pin, exp)
    return jsonify(sid = sid)


@app.route('/get/<sid>/<int:pin>', methods = ['GET'])
def get(sid, pin):
    logger.debug("Obtain msg from the database")
    msg = lib.get_secret(sid, pin)
    if len(msg) > 0:
        logger.debug("Message obtained: " + msg)
        decrypted_msg = libencryption.decrypt(msg)
        return jsonify(msg = decrypted_msg)
    else:
        return '{"error":"not found"}', 404

@app.route('/del/<sid>/<int:pin>', methods = ['DELETE'])

def dels(sid, pin):
    if len(sid)>0:
        del_id = lib.del_secret(sid, pin)
        logger.debug("Sid succesfully deleted: " + str(del_id))
    else: print("Sid does not exist")
    logger.debug('End my super App')
    return jsonify(deleted_sid = sid)

@app.errorhandler(404)
def not_found(error=None):
    logger.debug("Start app.errorhandler to confirm status 404")
    message = {
            'status': 404,
            'message': 'URL is wrong: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


