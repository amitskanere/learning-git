a = 'i am amit kanere'
b = a.split()
c = ''
for words in b[::-1]:
     c = c+" "+words[::-1]
print(c)