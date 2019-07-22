from flask import Flask, request, jsonify
import dblib
import logger_module
import libencryption
import sys

logger = logger_module.setup_logger("secret")

if libencryption.check_key():
    print("Starting my super App")
    logger.debug('Starting my super App')
else:
    print ('Cannot Find Server as file key.txt is not found')
    logger.debug('Cannot Find Server as file key.txt is not found')
    sys.exit("File key.txt is not found ")


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
    encrypted_msg = libencryption.encrypt(msg)
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
    # logger.debug("Delete data from database")
    deleted = dblib.del_secret(sid, pin)
    if deleted==1:
        logger.debug("Sid succesfully deleted: " + str(deleted))
        return  jsonify(deleted_sid=sid)
    else:
        return jsonify({
            'status': "404: request",
            'message':' not  deleted '})
# logger.debug('End my super App')



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
