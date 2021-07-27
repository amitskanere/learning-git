# a = list(range(1, 101))
# print(a)
# for value in range(1, len(a) + 1):
#     a[-value] = value
# print(a)
# #

# a=list(range(1,101))
# for index,value in enumerate(a):
#     if value%2==0:
#         a.append(a[index])
#         del a[index]
#
# print(a)
#
# a=[1,1,1,1,0,0,2,1,1,1,2]
# for index,value in enumerate(a):
#     if value==1:
#         del a[index]
#         a.insert(a[index],value)
#
#     elif value==2:
#         del a[index]
#         a.append(value)
#
# print(a)

#sum of diagonal value in a matrix
# a=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# n = len(a)
# d1=0
# d2=0
# c=2
# for value in range(0,n):
#     c=c-1
#     d1=d1+a[value][c]
#     d2=d2+a[value][value]
# print(a)
# print(f'sum of diagonal 1 :{d1}')
# print(f'sum of diagonal 2 : {d2}')

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friens_food=my_foods[:2]
# my_foods.append('donut')
# friens_food.append('ice cream')
# print(my_foods)
# print(friens_food)
# friens_food=my_foods
# print(my_foods)
# print(friens_food)
