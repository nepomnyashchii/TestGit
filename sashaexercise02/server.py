from flask import Flask, jsonify
import datetime

import lib
app = Flask(__name__)
print("\n\n\n\n\n")


@app.route('/')
def index():
    count = 4
    simpleList = []
    news = lib.get_news(count)
    simpleList.append(news)
    norris = lib.get_norris(count)
    simpleList.append(norris)
    return jsonify(
        data=simpleList,
        time=datetime.datetime.now()
    )
