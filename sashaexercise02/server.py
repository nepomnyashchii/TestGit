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
    return jsonify(
        news=news,
        norris=norris,
        time=datetime.datetime.now()
    )
