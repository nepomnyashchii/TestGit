import lib_copy


new_id = lib_copy.insert_todo("jopa")
print(new_id)

all_data = lib_copy.get_all()
print(all_data)

one = lib_copy.get_todo_by_id(new_id)
print(one)

updated = lib_copy.update_todo_by_id(new_id, "FFF", 1)
print(updated)

response = lib_copy.delete_todo_by_id(new_id-1)
print(response)
