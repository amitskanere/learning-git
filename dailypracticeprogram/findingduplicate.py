a='am bd d h u'
b=a.split()
print(b)
c=set(a)
c=list(c)
print(c)
if len(a)==len(c):
    print('no duplicate')
else:
    print("there is a duplicate")

