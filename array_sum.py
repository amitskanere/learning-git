


def sum_of_array(arr):
    sum=0
    for i in arr:
        sum=sum+i

    return sum

arr=[1,4,2,4,2,4,9,8]
ans = sum_of_array(arr)
print("sum of array :",ans)