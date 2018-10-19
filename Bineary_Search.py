import time
def Bineary_Search(list1,e):
    found = False
    h = len(list1)
    l = 0
    while l <= h and not found:
        mid = int((h+l)/2)
        if list1[int(mid)] == e:
            found = True
        elif list1[int(mid)] < e:
            l = mid + 1
        else:
            h = mid - 1
    return mid

list1 = []
n = int(input("Enter the number of elements in the list"))
for i in range(0,n):
    list1.append(int(input("Enter the list elements")))
e = int(input("Enter the element to be found"))
start_time = time.clock()
p = Bineary_Search(list1,e)
print("%s seconds " % (time.clock() - start_time))
if p:
    print("Element ",e," Found at ",p+1)
else:
    print("Element not found")
