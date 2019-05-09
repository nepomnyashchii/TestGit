from flask import Flask, jsonify
import datetime

import lib
app = Flask(__name__)
print("\n\n\n\n\n")


@app.route('/')
def index():
    return 'Flow Runner :)'


@app.route('/run/<string:username>/<string:flow>')
def run(username, flow):
    data = lib.get_flowdata(username, flow)
    # sampledata = [(u'news:3', 1), (u'norris:3', 2)]
    # print(data)
    if not data:  # len(data) == 0:
        return jsonify(
            error="no data for this user and flow",
            username=username,
            flow=flow,
            time=datetime.datetime.now()
        )

    simpleList = []
    for line in data:
        action_data = lib.run_action(line)
        simpleList.append(action_data)

    return jsonify(
        data=simpleList,
        username=username,
        flow=flow,
        time=datetime.datetime.now()
    )
