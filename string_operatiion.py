a = "amit kaner chetan ashish"
print(a.split())

remot_file = open("E:\\lectures\\python\\programs\\remote_new_file.txt")

lines = remot_file.readlines()

print(lines)

ignore_name = {
    "chetan",
    "ashish",
}

for line in lines:
    # print(line)

    each_name = line.split()

    for name in each_name:
        if name not in ignore_name:
            print(name)



remot_file.close()