import lib
# import jsonify

new_id = lib.insert_todo("jopa")
print(new_id)

all_data = lib.get_todo()
print(all_data)

one = lib.get_todo_by_id(new_id)
print(one)


# return jsonify(
# data=data,
#     )

# data = lib.delete_todo()
# print(data)

# data =lib.update_todo()
# print(data)
