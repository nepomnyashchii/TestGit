import lib

chairs= "italian"
tables = "french"

novel_id = lib.insert_furniture(chairs, tables)
print(novel_id)

all_data = lib.get_everything()
print(all_data)

id_furniture = lib.get_furniture_by_id(novel_id)
print(id_furniture)


updated = lib.update_furniture_by_id(novel_id, "spanish", "german")
print(updated)

delete_previous_id = lib.delete_furniture_by_id(novel_id-1)
print(delete_previous_id)
