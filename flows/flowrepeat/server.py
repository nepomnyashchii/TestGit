from flask import Flask, jsonify
import datetime

import lib
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
print("\n\n\n\n\n")


@app.route('/')
def index():
    return 'Flow Runner :)'


@app.route('/run/<string:username>/<string:flow>')
def run(username, flow):
    data = lib.get_flowdata(username, flow)
    # data = [(u'news:3', 1), (u'norris:3', 2)]
    print(data)
    if not data:  # len(data) == 0:
        return jsonify(
            error="no data for this user and flow",
            username=username,
            flow=flow,
            time=datetime.datetime.now()
        )

    simple_list = []
    for idx, line in enumerate(data):
        actionline = line[0]
        print(actionline)
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
    return jsonify(
        username=username,
        flow=flow,
        time=datetime.datetime.now(),
        data=simple_list
    )

