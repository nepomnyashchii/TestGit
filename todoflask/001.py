from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

print("\n\n\n\n\n\n\n\n\n\n")


@app.route('/')
def index():
    return 'Flow Runner :)'


# @app.route('/todo', methods = ['POST'])
# def insert_todo():
#     return "You said: " + request.form['text']

# @app.route("/echo", methods=['POST'])
# def echo():
#     return "You said: " + request.form['text']

@app.route("/echo", methods=['POST'])
def echo():
    r = requests.post('https://httpbin.org/post', data = {'key':'value'})
    return "You said: "+ request.form["text"]