import time
list1 = []
n = int(input("Enter the number of elements in the list"))
for i in range(0,n):
    list1.append(int(input("Enter the list elements")))

start_time = time.clock()
for i in range(1, len(list1)):
    j = i
    while j > 0 and list1[j] < list1[j - 1]:
        temp = list1[j]
        list1[j] = list1[j-1]
        list1[j-1] = temp
        j = j - 1
print("%s seconds" % (time.clock() - start_time))
print("Sorted list is")
print(list1)