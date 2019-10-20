import json



# def pretty(d, indent=0):
#    for key, value in d.items():
#       print('\t' * indent + str(key))
#       if isinstance(value, dict):
#          pretty(value, indent+1)
#       else:
#          print('\t' * (indent+1) + str(value))



with open("data.json") as f:
    json_str = f.read()

# with open('data.json') as json_file:
#     data = json.load(json_file)

count = 0
for char in json_str:
    if char == 'a':
        count += 1
print(count)

json_data = json.loads(json_str)


# glossary = json_data["glossary"]
# str_count = input("Please enter count:")
# count = int(str_count)
# new_json_data = {}
# for i in range(1, count+1):
#     new_json_data["glossary" + str(i)] = glossary

# with open("data2.json", "w") as f:
#     f.write(json.dumps(new_json_data, indent=4))



def pretty2 (d, indent=0):
    for key, value in d.items():
        print('\t' * (indent+1) + "Key:" + str(key))
        if isinstance(value, dict):
            pretty2(value,indent+1)
        else:
            print('\t' * (indent+1) + "Val:" + str(value))



pretty2(json_data)
