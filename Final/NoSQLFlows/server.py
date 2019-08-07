from flask import Flask, request, jsonify
import datetime
import lib
import logger_module
logger = logger_module.setup_logger("flowsapp")
logger.debug('Start my super App')


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

print("\n\n\n\n\n\n\n\n\n\n")


@app.route('/')
def index():
    return 'Flow Runner :)'


# ------------------------------
# -------- GET FLOW ----------
# ------------------------------


@app.route('/run/<string:username>/<string:flow>')
def run(username, flow):
    logger.debug('run invoked')
    data = lib.get_flowdata(username, flow)

    simple_list = []
    for idx, line in enumerate(data):
        actionline = line
        action_data = lib.run_action(actionline)

        simple_list.append({
            "action": idx,
            "type": actionline.split(":")[0],
            "data": action_data
        })
    logger.debug("Action_data: " + str(action_data))
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
    logger.debug("Start app.errorhandler to confirm status 404")
    message = {
        'status': 404,
        'message': 'URL is wrong: ' + request.url,
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
    logger.debug("Status 405 found with errorhandler")
    return resp


# {
#     "name": "alex",
#     "phone": "234",
#     "flows": [
#         {
#             "goodmorning": [
#                 "news:3",
#                 "norris:3",
#                 "coctail:random",
#                 "weather:Brooklyn, NY"
#             ]
#         },
#         {
#             "hi": [
#                 "news:3",
#                 "norris:3",
#                 "coctail:random",
#                 "weather:Brooklyn, NY"
#             ]
#         }
#     ]
# }
