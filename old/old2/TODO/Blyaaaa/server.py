
from flask import Flask, request, jsonify
import json
import libtry2
import logger_module
logger = logger_module.setup_logger("todo2")
logger.debug('Start my super App')

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

print("\n\n\n\n\n\n\n\n\n\n")


@app.route('/')
def index():
    return 'Flow Runner :)'
# get data through todo (not forget to transfer obtained tupple to the string)


@app.route('/todo')
def get_todo():
    logger.debug('run invoked')
    all_data = libtry2.get_all()
    logger.debug("get information from all ids: " + str(all_data))
    print(all_data)
    return jsonify(data_for_all_ids=str(all_data))


@app.route('/todo', methods=['POST'])
def insert_todo():
    logger.debug("Insert is invoked")
    result = request.json
    print(result)
    data = result["text"]
    logger.debug("Information from the body: " + str(data))
    print(data)
    new_id = libtry2.insert_todo(data)
    logger.debug("Inserted id: " + str(new_id))
    print(new_id)
    return jsonify(new_id=str(new_id))


@app.route('/todo/<int:id>', methods = ['PUT'])
def update_todo(id):
    result= request.json
    logger.debug("Information from the body: " +str(result))
    print(result)
    new_result=result["text"]
    print(new_result)
    logger.debug("Information for updated text from dictionary: " + str(new_result))
    new_data=result["done"]
    logger.debug("Information for true or false from dictonary: " + str(new_data))
    new_information_id = libtry2.update_todo_by_id(id, new_result, new_data)
    logger.debug("updated id: " + str(new_information_id))
    print(new_information_id)
    return jsonify(new_information_id= str(new_information_id))


@app.route('/todo/<int:id>')
def get_all_forid_delete_previous_id(id):
    logger.debug("Get all information by id")
    id_data = libtry2.get_todo_by_id(id)
    logger.debug("Provide all information for asked id: " + str(id_data))
    print(id_data)
    delete_previousid = lib.delete_todo_by_id(id-1)
    logger.debug(
        "Requested operation to delete the data successfully accomplished")
    return jsonify(id_data = str(id_data),
    previous_data = "previous data successfully deleted")

# {
#     "text":"asdasd",
#     "done":true
# }

# {"text":"asdasdasd"}
