a='am bd d h db bd u'
b=a.split()
print(b)
c = set(b)
print(c)
if len(b)==len(c):
    print('no duplicate')
else:
    print("there is a duplicate")

