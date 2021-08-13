a = [8, 3, 1, 3, 6, 4, 5, 6, 8, 9, 2, 1, 4]
b = []
c = []
for number in a:
    if number not in b:
        b.append(number)
    else:
        c.append(number)

print('duplicate numbers are', c)

print("D")