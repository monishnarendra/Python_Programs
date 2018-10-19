import time
def Linear_Search(list1,e):
    p = 0
    found = False
    while p <len(list1) and not found:
        if list1[p] == e:
            found = True
        p = p + 1
    return p

list1 = []
n = int(input("Enter the number of elements in the list"))
for i in range(0,n):
    list1.append(int(input("Enter the list elements")))
e = int(input("Enter the element to be found"))
start_time = time.clock()
p = Linear_Search(list1,e)
print("%s seconds " % (time.clock() - start_time))
if p:
    print("Element ",e," Found at ",p)
else:
    print("Element not found")
