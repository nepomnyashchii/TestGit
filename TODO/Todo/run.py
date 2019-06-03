import lib


new_id = lib.insert_todo("jopa")
print(new_id)

all_data = lib.get_todo()
print(all_data)

one = lib.get_todo_by_id(new_id)
print(one)

updated = lib.update_todo_by_id(new_id, "FFF", 1)
print(updated)

response = lib.delete_todo_by_id(new_id-1)
print(response)
