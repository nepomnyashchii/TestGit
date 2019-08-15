from flask import Flask, flash, redirect, render_template, request, session, abort, json

app = Flask(__name__)


@app.route("/")
def index():
    return "Flask App!"


@app.route("/news")
def news():
    quote = {
        'quote': (
            "I've always been more interested in "
            "the future than in the past."
        ),
        'author': 'Grace Hopper'
    }
    json = '{"name":"alex","age":32}'
    return render_template('news.html', news=json, quote=quote["quote"])


@app.route("/hello/<string:name>")
def hello(name):
    
    return render_template('test.html', name=name)


# if __name__ == "__main__":
#     app.run()
    # app.run(host='0.0.0.0', port=80)


# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def index():
#     return "Index!"


# @app.route("/hello")
# def hello():
#     return "Hello World!"


# @app.route("/members")
# def members():
#     return "Members"


# @app.route("/members/<string:name>")
# def getMember(name):
#     return '<input type="text"/><button value="asd">push me</button><h1>name</h1><br/><h2>name</h2>'


# if __name__ == "__main__":
#     app.run()
