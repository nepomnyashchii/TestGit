
data = [10, "mama", (1, 2, 3), {"a": "mama", "b": "papa"}]
for element in data:
    if str(type(element)) == "<type 'int'>":
        element = element*2
    print(str(element), type(element))
