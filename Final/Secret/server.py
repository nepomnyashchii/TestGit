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
    print('Cannot Find Server as file key.txt is not found')
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
    if request.json is None \
            or request.json is not None \
            and ("msg" not in request.json.keys() or "pin" not in request.json.keys() or "exp" not in request.json.keys()):
            return jsonify({
            'status': "404: request",
            'message': 'Invalid Body url: ' + request.url,
        })
    else:
        result = request.json
        msg = result["msg"]
        pin = result["pin"]
        exp = result["exp"]
    encrypted_msg = libencryption.encrypt(msg)
    sid = dblib.put_secret(encrypted_msg, pin, exp)
    logger.debug("put from a post return sid=" + sid)
    # return jsonify(sid=sid)
    if len(str(sid))>0:
        return jsonify (sid=sid)
    else:
        return jsonify (sid = sid,
        Data="Data is not received from DB")



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
    return returnMessage(dblib.get_secret(sid, pin))

# ------------------------------
# -------- GET SECRET (BODY)----
# ------------------------------


@app.route('/secret', methods=['GET'])
def get_secret_body():
    logger.debug("/secret GET with BODY invoked")
    if request.json is None \
            or request.json is not None \
            and ("sid" not in request.json.keys() or "pin" not in request.json.keys()):
        return jsonify({
            'status': "Bad request",
            'message': 'invalid body url=' + request.url,
        }), 400
    else:
        return returnMessage(dblib.get_secret(request.json["sid"], request.json["pin"]))


# ------------------------------
# -------- GET SECRET helper----
# ------------------------------

def returnMessage(msg):
    if len(msg) > 0:
        logger.debug("Message obtained: " + msg)
        decrypted_msg = libencryption.decrypt(msg)
        return jsonify(msg=decrypted_msg)
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
    if deleted:
        logger.debug("Sid succesfully deleted: " + str(deleted))
        return jsonify(deleted_sid=sid)
    else:
        return jsonify({
            'status': "404: request",
            'message': 'Such Sid and/or pin does not exist'})


# ------------------------------
# -------- DEL SECRET ----------
# ------------------------------

@app.route('/secret', methods=['DELETE'])
def delete_secret():
    return jsonify(Data='Not implemented yet'), 404

# # ------------------------------
# # -------- CHECK ROUTE /SECRET ----------
# # ------------------------------

# @app.route('/secret', methods=['PUT', 'PATCH', 'COPY', 'HEAD' ])
# def invalid_method_request_secret():
#     if request.method == 'PUT' or 'PATCH'or 'COPY' or'HEAD':
#         return jsonify(Data='Invalid request.method'), 404

# # ------------------------------
# # -------- CHECK ROUTE / ----------
# # ------------------------------

# @app.route('/', methods=['POST', 'DELETE','PUT', 'PATCH', 'COPY', 'HEAD' ])
# def invalid_method_request():
#     if request.method == 'POST' or 'DELETE' or 'PUT' or 'PATCH'or 'COPY' or'HEAD':
#         return jsonify(Data='Invalid request.method'), 404

# # ------------------------------
# # -------- CHECK ROUTE /SECRET/SID/PIN ----------
# # ------------------------------

# @app.route('/secret/<sid>/<int:pin>', methods=['POST','PUT', 'PATCH', 'COPY', 'HEAD' ])
# def invalid_method_request_id_pin():
#     if request.method == 'POST' or 'DELETE' or 'PUT' or 'PATCH'or 'COPY' or'HEAD':
#         return jsonify(Data='Invalid request.method'), 404


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



@app.errorhandler(405)
def invalid_method(error=None):
    logger.debug("405 errorhandler invoked for:" + request.url)
    message = {
        'status': 405,
        'message': '405 Method Not Allowed: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 405
    return resp
