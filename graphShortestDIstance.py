import heapq
def dijkstra(graph,start,end):
    pq , dist , prev = [(0,start)],{v : float('inf') for v in graph },{}
    dist[start] = 0
    
    while pq :
        d , u = heapq.heappop(pq)
        if u == end :
            break
        for v , w in graph[u].items():
            new_dist = d + int(w)
            if (new_dist< dist[v]):
                dist[v],prev[v] = new_dist , u
                heapq.heappush(pq,(dist,v))
    
    path, u = [] ,end
    while u in prev:
        path.insert(0,u)
        u = prev[u]
        
    return ([start]+path,dist[end]) if path else ([],float('inf'))
    
graph = {input().strip() : {} for _ in range (int(input("Enter the number of Location :")))}
for _ in range (int(input("Enter the Number of Path : "))):
    u , v , w = input().split()
    graph[u][v] = graph[v][u] = int(w)
start,end = input("Enter start and End").split()
path, time = dijkstra(graph,start,end)
print("Path : ","->".join(path)if path else "None","\nTime",time)
