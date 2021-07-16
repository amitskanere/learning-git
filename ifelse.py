price=1000000
is_good_credit=True
if is_good_credit:
    price=price*.10
else:
    price=price*.20
print("your down payment is "+ str(price))
