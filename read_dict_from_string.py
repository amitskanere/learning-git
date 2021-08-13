import json
data = """[{"name":"chetan","age":23},{"name":"chetan","age":23},{"name":"chetan","age":23},
        {"name":"chetan","age":23}] """


my_dict_data = json.loads(data)

print(my_dict_data)

print(json.dumps(my_dict_data))