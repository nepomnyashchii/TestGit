
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

@app.route('/todo/<int:id>')
def get_all(id):
    id_data = lib.get_todo_by_id(id)
    print(id_data)
    return str(id_data)

@app.route('/todo', methods = ['POST'])
def insert_todo():
    result = request.json
    data= result["text"]
    # jsonify(result)
    new_id = lib.insert_todo(json.dumps(data))
    print(new_id)
    return jsonify(new_id=str(new_id))
    # return jsonify(
    #     data=data,
    # )
@app.route('/todo/<int:id>', methods = ['PUT'])
def update_todo(id):
    result = request.json
    new_result=result["text"]
    new_information_id = lib.update_todo_by_id(id, json.dumps(new_result), 1)
    print(new_information_id)
    return jsonify(new_information_id= str(new_information_id))
    # delete_previous_id = lib.delete_todo_by_id(id-1)
    # print (delete_previous_id)
    # print(data)
    # return jsonify(
    #     data=data,
    # )


# {
#     text:"asdasd",
#     done:true
# }



