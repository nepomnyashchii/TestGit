from flask import Flask, request, jsonify
import dblib
import logger_module
import libencryption
import os.path


logger = logger_module.setup_logger("secret")
logger.debug('Starting my super App')
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['APPLICATION_ROOT'] = '/api'
print("\n\n\n")


@app.route('/')
def index():
    logger.debug("Request for testing connection invoked")
    return 'Cool API is online :)'


@app.route('/ping')
def ping():
    logger.debug("Request for ping")
    return jsonify(data='pong'), 200

# ------------------------------
# ------- SECRET ROUTES --------
# ------------------------------

# ------------------------------
# ------- ADD SECRET ----------
# ------------------------------

@app.route('/secret', methods=['POST'])
def add_secret():
    logger.debug("Invoke: put from a post")
    result = request.json
    msg = result["msg"]
    pin = result["pin"]
    exp = result["exp"]
    # if libencryption.key(msg):
    #     encrypted_msg = libencryption.encrypt(msg)
    # else:
    #     return {"File is not found"}
    if os.path.isfile('key.txt'):
        encrypted_msg = libencryption.encrypt(msg)
    else:
        # raise FileNotFoundError
        return jsonify("File does not exist")
    sid = dblib.put_secret(encrypted_msg, pin, exp)
    logger.debug("put from a post return sid=" + sid)
    return jsonify(sid=sid)


# Old Put - method=GET
# @app.route('/secret/put/<msg>/<int:pin>/<int:exp>', methods=['GET'])
# def put(msg, pin, exp):
#     encrypted_msg = libencryption.encrypt(msg)
#     logger.debug("Invoke: put a get")
#     sid = dblib.put_secret(encrypted_msg, pin, exp)
#     logger.debug("Obtain sid: " + sid)
#     return jsonify(sid=sid)


# ------------------------------
# -------- GET SECRET ----------
# ------------------------------

@app.route('/secret/<sid>/<int:pin>', methods=['GET'])
def get_secret_query(sid, pin):
    logger.debug("/secret GET invoked")
    msg = dblib.get_secret(sid, pin)
    if len(msg) > 0:
        logger.debug("secret obtained from DB: " + msg)
        decrypted_msg = libencryption.decrypt(msg)
        logger.debug("/secret GET returned OK")
        return jsonify(msg=decrypted_msg)
    else:
        logger.debug("/secret GET returned 404")
        return jsonify({
            'status': "404: request",
            'message': 'pin or sid is wrong: ' + request.url,
        })

# ------------------------------
# -------- GET SECRET (BODY)----
# ------------------------------

@app.route('/secret', methods=['GET'])
def get_secret_body():
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
            'status': "200: request",
            'message': 'pin or sid is wrong: ' + request.url,
        })


# ------------------------------
# -------- DEL SECRET ----------
# ------------------------------

@app.route('/secret/<sid>/<int:pin>', methods=['DELETE'])
def del_secret(sid, pin):
    logger.debug("Delete data from database")
    if len(sid) > 0:
        del_id = dblib.del_secret(sid, pin)
        logger.debug("Sid succesfully deleted: " + str(del_id))
        return jsonify(deleted_sid=sid)
    else:
        return jsonify({
            'status': "200: request",
            'message': 'pin or sid is wrong: ' + request.url,
        })

    logger.debug('End my super App')



# ------------------------------
# -------- DEL SECRET ----------
# ------------------------------

@app.route('/secret', methods=['DELETE'])
def delete_secret():
    return jsonify(data='Not implemented yet'), 404


# ------------------------------
# -------- errorhandler  -------
# ------------------------------

@app.errorhandler(404)
def not_found(error=None):
    logger.debug("404 errorhandler invoked for:" + request.url)
    message = {
        'status': 404,
        'message': 'URL not found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
