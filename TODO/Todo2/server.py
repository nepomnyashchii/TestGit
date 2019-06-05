
from flask import Flask, request, jsonify
import json
import lib

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

print("\n\n\n\n\n\n\n\n\n\n")


@app.route('/')
def index():
    return 'Flow Runner :)'
# get data through todo (not forget to transfer obtained tupple to the string)

@app.route('/todo')
def get_todo():
    all_data = lib.get_all()
    print(all_data)
    return str(all_data)

@app.route('/todo/run/<int:id>')
def get_all(id):
    id_data = lib.get_todo_by_id(id)
    print(id_data)
    return str(id_data)

@app.route('/todo', methods = ['POST'])
def insert_todo():
    result = request.json
    data= result["text"]
    print(data)
    new_id = lib.insert_todo(data)
    print(new_id)
    return jsonify(new_id=str(new_id))

@app.route('/todo/<int:id>', methods = ['PUT'])
def update_todo(id):
    result= request.json
    new_result=result["text"]
    new_data=result["done"]
    new_information_id = lib.update_todo_by_id(id, new_result, new_data)
    print(new_information_id)
    return jsonify(new_information_id= str(new_information_id))

@app.route('/todo/<int:id>')
def delete_todo(id):
    delete_previousid = lib.delete_todo_by_id(id-1)
    return "data deleted"

# {
#     "text":"asdasd",
#     "done":true
# }

# {"text":"asdasdasd"}





