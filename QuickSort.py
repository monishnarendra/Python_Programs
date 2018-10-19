import random

def quicksort(list1):
    if len(list1) > 1:
        high,low,equal=[],[],[]
        pivot = list1[0]
        for i in list1:
            if pivot < 0:
                low.append(i)
            if pivot == 0:
                equal.append(i)
            if pivot > 0:
                high.append(i)
        return quicksort(low)+equal+quicksort(high)
    else:
        return list1

n = int(input("Enter the number of elements"))
x = int(input("Enter the range"))
list1=[]
for i in range(n):
    list1.append(int(random.random()*x))
print(list1)
print(quicksort(list1))