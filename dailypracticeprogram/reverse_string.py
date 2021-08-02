a=range(1,101)
list_a=list(a)
print(f'list of 100 numbers = {list_a}')
l=[]
for number in range(len(list_a)-1,-1,-1):
    l.append(list_a[number])
print(f'reverse of a list = {l}')

#this expression also returns a reverse of a list
print(list_a[::-1])



b='thisisastringexample'
print(f'string = {b}')
revers=''
for value in range(1,len(b)+1):
    revers=revers+b[-value]

print(f'reverse string = {revers}')