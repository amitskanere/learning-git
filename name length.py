name=input("enter your name ")
if  len(name)<3:
    print("name must be atleast 3 character long")
elif len(name)>50:
    print("name must be less than 50 characters")
else :
    print("name looks good")