import telebot
import lib

bot =telebot.TeleBot("873802609:AAGrF4tID-CD4lufzgMjqNEnqLxhCaEweLM")

bot.message_handler(content_types=['text'])

def get_all():
    all_data = lib.get_all()
    return bot.send_message(message.chat.id, all_data)

# id_data = lib.get_todo_by_id(id)

# bot.polling (none_stop = True)

# result = request.json
# data = result["text"]
# new_id = lib.insert_todo(data)

# result= request.json
# logger.debug("Data from the body: " +str(result))
# new_result=result["text"]
# logger.debug("Data for updated text from dictionary: " + str(new_result))
# new_data=result["done"]
# logger.debug("Data for true or false from dictonary: " + str(new_data))
# new_information_id = lib.update_todo_by_id(id, new_result, new_data)
# logger.debug("Updated id: " + str(new_information_id))
# return jsonify(id= new_information_id)

# @app.route('/todo/<int:id>', methods =['DELETE'])
# def delete_todo(id):
#     logger.debug("Run invoked to delete data for certain id from the database")
#     delete_id = lib.delete_todo_by_id(id)
#     logger.debug("Requested operation to delete the data successfully accomplished")
#     return jsonify(id="Data successfully deleted")


# @app.errorhandler(404)
# def not_found(error=None):
#     logger.debug("Start app.errorhandler to confirm status 404")
#     message = {
#             'status': 404,
#             'message': 'URL is wrong: ' + request.url,
#     }
#     resp = jsonify(message)
#     resp.status_code = 404

#     return resp

# {
#     "text":"asdasd",
#     "done":true
# }

# {"text":"asdasdasd"}

