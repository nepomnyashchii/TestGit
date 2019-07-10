from flask import Flask, jsonify
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
