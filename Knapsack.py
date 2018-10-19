values = list(map(int,input("Enter the values").split()))
weight = list(map(int,input("Enter the weight").split()))
list1 = []
sack = []
n = len(weight)
W = int(input("Enter the Max weight"))
w = 0
for i in range(n+1):
    list2=[0 for x in range(W+1)]
    list1.append(list2)

for i in range(1,n+1):
    item = i-1
    for w in range(1,W+1):
        if weight[item] <= w:
            list1[i][w] = max(list1[i-1][w],values[item]+list1[i-1][w-weight[item]])
        else:
            list1[i][w] = list1[i-1][w]

i = n
w = W
while i > 0 and w > 0:
    if list1[i][w] == list1[i-1][w]:
        i = i-1
        pass
    else:
        sack.append(i)
        w = w-weight[i-1]
        i = i-1

for i in range(n+1):
    for j in range(W+1):
        print(list1[i][j],end='\t')
    print()

print("value = ",list1[-1][-1])
print("items are ",sack)