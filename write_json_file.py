import json
data = [{"name":"chetan","age":23},{"name":"chetan","age":23},{"name":"chetan","age":23},
        {"name":"chetan","age":23}] * 100
fp = open("emp_list_2.json", mode="w" )

json.dump(data,fp,indent=1)

fp.close()
