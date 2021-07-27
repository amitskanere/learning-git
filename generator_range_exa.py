def generate_value(starvalue , endvalue , step):
    limit = endvalue
    count = starvalue
    while count < limit:
        yield count
        # print("increasing count")
        count = count + step

for value in generate_value(1,10,2):
    print(value)