# # list_of_number=[]
# # for value in range(1,101):
# #     list_of_number.append(value)
# # print(list_of_number)
#
#
#
# number = int(input('please enter a number :'))
# status = True
# for num in range(2, number):
#     if number%num==0:
#         status=False
# if status:
#     print('nubmer is prime')
#
# else :
#     print('number is not prime')

a = range(1,100)
prime_numbers = []
for value in a:
    # print(value)

    status = True

    for index in range(2,value):

        if value % index == 0:
            status = False
            break

    if status:
        prime_numbers.append(value)

print(prime_numbers)
