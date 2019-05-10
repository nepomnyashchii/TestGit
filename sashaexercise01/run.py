from flask import Flask, request, json, jsonify
import lib
# print(__name__)
app = Flask(__name__)


@app.route('/')
def index():
    return 'Flow Run :)'


@app.route('/run/<string:username>/<string:flow>')
def run(username, flow):
    # data = lib.get_mixedtables(username, flow)
    data = [(u'news:5', 1), (u'norris:6', 2)]
    return jsonify(
        data=data,
        username=username,
        flow=flow
    )
