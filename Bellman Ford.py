def bellmanford(s):
    dist[s] = 0
    for i in range(v-1):
        for j in graph:
            dist[j[2]] = min(dist[j[2]],dist[j[1]]+j[0])
            print(dist[1:])

v = int(input("Enter the number of Vertex"))
e = int(input("Enter the number of Edges"))
print("Enter -- u v w")
graph = []
dist = [9999 for i in range(0,v+1)]

for i in range(e):
    u, v, w = map(int,input().split())
    graph.append((w,u,v))

s = int(input("Enter the source node"))
print(graph)
bellmanford(s)
print("Shortest path is..",dist[1:])