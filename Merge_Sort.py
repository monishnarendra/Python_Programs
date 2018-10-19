import random
import time

def merge_sort(list1):
    if len(list1) > 1:
        mid = len(list1)/2
        left = merge_sort(list1[:int(mid)])
        right = merge_sort(list1[int(mid):])
        return merge(left,right)
    else:
        return list1

def merge(left,right):
    if not len(left) or not len(right):
        return left or right
    result =[]
    i,j = 0,0
    while len(result) < len(left) + len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i =i+1
        else:
            result.append(right[j])
            j = j+1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result
list1 = []
list2 = []
n = int(input("Enter the numebr of elements"))
x = int(input("Enter the range"))
for i in range(n):
    list1.append(int(random.random()*x))
t = time.clock()
list2 = merge_sort(list1)
print(list2)
print(time.clock()-t)