num = input("Enter a number : ")
p=len(num)
a=0
for value in num:
    n=int(value)
    a=a+pow(n,p)
if a==int(num):
    print("number is amstrong")
else:
    print("number is not amstrong")



