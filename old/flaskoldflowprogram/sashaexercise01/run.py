from flask import Flask, request, json, jsonify
import lib
import datetime
# print(__name__)
app = Flask(__name__)


@app.route('/')
def index():
    return 'Flow Run :)'


@app.route('/run/<string:username>/<string:flow>')
def run(username, flow):
    # data = lib.get_mixedtables(username, flow)
    # return jsonify(
    #     data=data,
    #     username=username,
    #     flow=flow)

    data = [(u'news:5', 1), (u'norris:6', 2)]
    print(data)
    simpleList = []
    for line in data:
        action_data = lib.run_action(line)
        simpleList.append(action_data)
    count = 4
    news = lib.get_news(count)
    norris = lib.get_norris(count)

    return jsonify(
        data=simpleList,
        username=username,
        flow=flow,
        time=datetime.datetime.now()
    )


