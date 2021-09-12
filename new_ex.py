def mergesort(unsortedlist):
     if len(unsortedlist) <=1:
          return unsortedlist
     middle = len(unsortedlist)//2
     left_list = unsortedlist[:middle]
     right_list = unsortedlist[middle:]

     left_list = mergesort(left_list)
     right_list = mergesort(right_list)
     return list(merge(left_list,right_list))
def merge(left_half,right_half):
     res =[]
     while len(left_half) != 0 and len(right_half) != 0:
          if left_half[0] < right_half[0]:
               res.append(left_half[0])
               left_half.remove(left_half[0])
          else:
               res.append(right_half[0])
               right_half.remove(right_half[0])
     if len(left_half) == 0:
          res = res + right_half
     else:
          res = res + left_half

     return res

unsortedlist = [23,45,2,98,56,83,67,29,74]     
print(mergesort(unsortedlist))

     

     