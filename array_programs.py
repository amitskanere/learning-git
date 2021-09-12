
# def sumofarray(arr):
#     sum=0
#     for i in arr:
#         sum += i
#     return sum


# def maxofarray(arr,n):
#     max = arr[0]
#     for i in range(1,n):
#         if i>max:
#             max=arr[i]
#     return max

def rotatearray(arr,n,d):
    temp=[]
    i=0
    while i<d:
        temp.append(arr[i])
        i=i+1

    i=0
    while d<n:
        arr[i]=arr[d]
        i=i+1
        d=d+1
    arr[:]=arr[:i]+temp
    return arr

arr=[1,2,3,4,5,6,7,8,9,10]
print(rotatearray(arr,len(arr),5))
