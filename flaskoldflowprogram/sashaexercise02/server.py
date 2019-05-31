from flask import Flask, jsonify
import datetime


import lib
app = Flask(__name__)
print("\n\n\n\n\n")


@app.route('/')
def index():
    count = 4
    news = lib.get_news(count)
    norris = lib.get_norris(count)
    return_data = {
        "news": news,
        "norris": norris
    }
    return jsonify(
        data=return_data,
        time=datetime.datetime.now()
    )
