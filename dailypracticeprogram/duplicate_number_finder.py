new_list=[1,2,3,9,4,5,6,1,7,8,9]
# unique_list = list(set(new_list))
unique_list=[]
duplicate_item=[]
for item in new_list:
    if item not in unique_list:
        unique_list.append(item)
    else:
        duplicate_item.append(item)



print(unique_list)
print(duplicate_item)
