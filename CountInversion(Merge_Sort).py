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

    result = []
    global count
    i=0
    j=0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i= i + 1
        else:
            result.append(right[j])
            count = count + (len(left)-i)
            j= j + 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result

list1 = []
list2 = []
count = 0
n = int(input("Enter the number of elements in the list"))
for i in range(0,n):
    list1.append(int(input("Enter the list elements")))

list2 = merge_sort(list1)
print(count)
print(list2)