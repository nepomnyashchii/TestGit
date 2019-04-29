from flask import Flask

app = Flask(__name__)
@app.route('/Hello/bye')
def index():
    return "zenit champion"