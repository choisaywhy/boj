import sys
from heapq import *

def solution(n,e,graph,u,v):
    
    def dijkstra(start):
        dist = [1e9]*(n+1)
        dist[start] = 0
        queue = [(dist[start],start)]
    
        while queue:
            cost, node = heappop(queue)

            if dist[node] < cost:
                continue

            for nxt, nxtcost in graph[node]:
                if dist[nxt] <= nxtcost + cost:
                    continue
                dist[nxt] = nxtcost + cost
                heappush(queue, (dist[nxt],nxt))
        
        return dist
    

    routes1 = dijkstra(1)
    routes2 = dijkstra(u)
    routes3 = dijkstra(n)

    ans = min(routes1[u] + routes2[v] + routes3[v], routes1[v] + routes2[v] + routes3[u])
    if ans < 1e9:
        print(ans)
    else:
        print(-1)






if __name__ == "__main__" :
    input = sys.stdin.readline
    n,e = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    u,v = map(int, input().split())
    solution(n,e,graph,u,v)