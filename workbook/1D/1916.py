import sys
from heapq import *

def solution(n,m,bus,s,d):
    cost = [1e9]*(n+1)
    cost[s] = 0
    queue = [(cost[s], s)]

    while queue:
        dist, node = heappop(queue)
        if cost[node] < dist:
            continue

        for v,w in bus[node]:
            if cost[v] <= dist + w:
                continue
            cost[v] = dist + w
            heappush(queue, (cost[v], v))
    
    print(cost[d])




if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    bus = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int, input().split())
        bus[u].append((v,w))
    s,d = map(int, input().split())
    
    solution(n,m,bus,s,d)