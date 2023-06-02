import sys
import heapq as hq

def solution(n,m,bus,a,b):

    queue = [(0,a)] # 비용, 현재 도시
    dist = [(1e11,[]) for _ in range(n+1)]
    dist[a] = (0,[a])

    while queue:
        cost, city = hq.heappop(queue)

        if dist[city][0] < cost:
            continue
    
        for v,w in bus[city]:
            if dist[v][0] <= cost + w:
                continue
            dist[v] = (cost + w, dist[city][1]+[v])
            hq.heappush(queue, (cost + w, v))
    
    print(dist[b][0])
    print(len(dist[b][1]))
    print(" ".join(map(str, dist[b][1])))







if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    bus = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int, input().split())
        bus[u].append((v,w))
    
    a,b = map(int, input().split())

    solution(n,m,bus,a,b)