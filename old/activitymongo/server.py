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
    # print(data)
    # data = [u'news:3', u'norris:3', u'coctail:random', u'weather:Brooklyn, NY']
    # data = [(u'weather:Brooklyn, NY',), (u'news:3',), (u'norris:3',), (u'news:2',), (u'thecocktail:random',), (u'thecocktail:random',)]
    # logger.debug("data from DB:" + str(data))
    # if not data:  # len(data) == 0:
    #     return jsonify(
    #         error="no data for this user and flow",
    #         username=username,
    #         flow=flow,
    #         time=datetime.datetime.now()
    #     )

    simple_list = []
    for idx, line in enumerate(data):
        actionline = line
        # print(actionline)
        action_data = lib.run_action(actionline)
        # print(action_data)
        simple_list.append({
            "action": idx,
            "type": actionline.split(":")[0],
            "data": action_data
        })

    # simpleList = []
    # for line in data:
    #     actionline = line[0]
    #     action_data = lib.run_action(actionline)
    #     simple_list.append(action_data)
    # weather_data =lib.run_weather(action)
    logger.debug("action data" + str(action_data))
    return jsonify(
        username=username,
        flow=flow,
        time=datetime.datetime.now(),
        data=simple_list
    )
