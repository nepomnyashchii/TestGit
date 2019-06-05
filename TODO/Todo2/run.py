import lib


new_id = lib.insert_todo("elephant")
print(new_id)

all_data = lib.get_all()
print(all_data)

new_id_data = lib.get_todo_by_id(new_id)
print(new_id)

updated = lib.update_todo_by_id(new_id, "monkey", 100)
print(updated)

delete_previousid = lib.delete_todo_by_id(new_id-1)
print(delete_previousid)
