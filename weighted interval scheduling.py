start = list(map(int,input().split()))
finish = list(map(int,input().split()))
weights = list(map(int,input().split()))
no = len(start)
items = [(x,y,z,j) for x,y,z,j in zip(finish,start,weights,range(no))]
items.sort()
print(items)
pred=[-1 for i in range(no)]
for i in range(no):
    j=i-1
    while(j>=0):
        if items[j][0]<=items[i][1]:
            pred[i]=j
            break
        j=j-1
print(pred)
lists=[0 for x in range(no)]
lists[0]=items[0][2]
for i in range(1,no):
        if pred[i]==-1:
            lists[i]=max(lists[i-1],items[i][2])
        else:
            lists[i]=max(lists[i-1],items[i][2]+lists[pred[i]])
print(lists)
i=len(lists)-1
lists.append(0)
sack=[]
while(i>=0):
    if(items[i][2]+lists[pred[i]]>=lists[i-1]):
        sack.append(items[i][3])
        i=pred[i]
    else:
        i=i-1
print("Answer=",lists[-2])
print("Items are ",sack)