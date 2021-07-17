numbers = [5,2,5,2,2]
for x_count in numbers :
    output=''
    for count in range(x_count) :
        output = output + '*'
    print(output)

for value in numbers:
    
    print("*" * value)


n = int(input("please enter the number"))
# print(type(n))

is_prime = True


for value in range(2,n-1):

    if n % value == 0:
        is_prime = False
        break

if is_prime:
    print("is prime")
else:
    print("Not a prime")
