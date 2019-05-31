from flask import Flask, jsonify
import libtodo

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

print("\n\n\n\n\n\n\n\n\n\n")


@app.route('/')
def index():
    return 'Flow Runner :)'
# get data through todo (not forget to transfer obtained tupple to the string)

@app.route('/todo')
def get_todo():
    data = libtodo.get_todo()
    print(data)
    return str(data)