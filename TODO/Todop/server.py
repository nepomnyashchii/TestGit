from flask import Flask, request, jsonify
import lib

app =Flask (__name__)

@app.route('/')

def try_first():
    return "my flask file"

@app.route('/todo')

def get_all ():
    all_data =lib.get_all()
    return jsonify(all_data=str(all_data))

@app.route('/todo/<int:id>')
def get_id (id):
    id_data = lib.get_id(id)
    return jsonify(my_id_data=str(id_data))

@app.route('/todo/<int:id>', METHODS = "POST")
def insert_id (id):
    result = request.json
    data = result["text"]
    new_id = lib.insert_todo(data)
    return jsonify(new_id=str(new_id))

@app.route('/todo/<int:id>', METHODS= "PUT")
def update_id (id):
    result =request.json
    data = result["text"]
    mydata = result["done"]
    new_information_id = lib.update_data(id, data, my_data)
    return jsonify(new_information_id =str(new_information_id))

@app.route('/todo/<int:id>', METHODS = "DELETE")
def delete_id (id):
    deleted_id = lib.delete_id(id)
    return jsonify(deleted_id = str(deleted_id))















