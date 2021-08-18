import json

fp = open("emp_list.json")

data = json.load(fp)

for value in data:
    print(value)
print(data)