import time
list1 = []
n = int(input("Enter the number of elements in the list"))
for i in range(0,n):
    list1.append(int(input("Enter the list elements")))
start_time = time.clock()
for i in range(0, len(list1)):
    p = i
    for j in range(i + 1,len(list1)):
        if list1[j] < list1[p]:
            p = j
        if p != i:
            temp = list1[i]
            list1[i] = list1[p]
            list1[p] = temp
print("--- %s seconds ---" % (time.clock() - start_time))
print("Sorted list is")
print(list1)