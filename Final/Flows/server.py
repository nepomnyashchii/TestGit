from flask import Flask, request, jsonify
import datetime
import lib
import logger_module
logger = logger_module.setup_logger("flowsapp")
logger.debug('Start my super App')

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['APPLICATION_ROOT'] = '/api'
print("\n\n\n")


@app.route('/')
def index():
    logger.debug("Request for testing connection invoked")
    return 'Flow runner is online :)'

# ------------------------------
# -------- GET FLOW ----------
# ------------------------------


@app.route('/flow/<string:username>')
def flow(username):
    logger.debug('Run invoked')
    data = lib.get_users(username)
    print(data)
    logger.debug("Data from DB(actionline):" + str(data))
    if not data:
        return jsonify(
            error="no data for this user and flow",
            username=username,
            time=datetime.datetime.now()
        )
    else:
        return jsonify(
            username=data,
            time=datetime.datetime.now()
        )


# ------------------------------
# -------- GET USER ----------
# ------------------------------

@app.route('/username/<string:flow>')
def user(flow):
    logger.debug('Run invoked')
    data = lib.get_flows(flow)
    print(data)
    logger.debug("Data from DB(actionline):" + str(data))
    if not data:
        return jsonify(
            error="no data for this user and flow",
            username=data,
            time=datetime.datetime.now()
        )
    else:
        return jsonify(
            flow=data,
            time=datetime.datetime.now()
        )


@app.route('/run/<string:username>/<string:flow>')
def run(username, flow):
    logger.debug('Run invoked')
    data = lib.get_flowdata(username, flow)
    print(data)
    logger.debug("Data from DB(actionline):" + str(data))
    if not data:
        return jsonify(
            error="no data for this user and flow",
            username=username,
            flow=flow,
            time=datetime.datetime.now()
        ), 404

    simple_list = []
    for idx, line in enumerate(data):
        actionline = line[0]
        logger.debug("Actionline: " + str(actionline))
        action_data = lib.run_action(actionline)
        simple_list.append({
            "action": idx,
            "type": actionline.split(":")[0],
            "data": action_data
        })

    logger.debug("Action data" + str(action_data))
    return jsonify(
        username=username,
        flow=flow,
        time=datetime.datetime.now(),
        data=simple_list
    )


# ------------------------------
# -------- GET USERNAME FLOW ----------
# ------------------------------

@app.route('/run/<string:username>')
def run_user(username):
    logger.debug('Run invoked')
    flow = "goodmorning"
    data = lib.get_flowdata(username, flow)
    print(data)
    logger.debug("Data from DB(actionline):" + str(data))
    if not data:
        return jsonify(
            error="no data for this user and flow",
            username=username,
            flow=flow,
            time=datetime.datetime.now()
        )

    simple_list = []
    for idx, line in enumerate(data):
        actionline = line[0]
        logger.debug("Actionline: " + str(actionline))
        action_data = lib.run_action(actionline)
        simple_list.append({
            "action": idx,
            "type": actionline.split(":")[0],
            "data": action_data
        })

    logger.debug("Action data" + str(action_data))
    return jsonify(
        username=username,
        flow=flow,
        time=datetime.datetime.now(),
        data=simple_list
    )

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
    logger.debug("Status 404 found with errorhandler")
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
    logger.debug("Status 405 found with errorhandler")
    return resp
