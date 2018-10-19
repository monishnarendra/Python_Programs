from heapq import *
def Djik(graph,start):
    n = len(graph)
    Q = [[0, start]]
    d = [999 for i in range(n)]
    d[start]=0
    while Q:
        [length, u] = heappop(Q)
        for v in range(n):
            if d[v] > d[u] + graph[u][v]:
                d[v] = d[u] + graph[u][v]
                heappush(Q, [d[v], v])
        print(d)
    return d
n=(int(input("Enter the size")))
graph = [[] for i in range(n)]
print(graph)
for j in range(n):
    for i in range(n):
        print("Enter cost of",i+1,"and",j+1)
        graph[i].append(int(input()))

print(graph)
print(Djik(graph,1))