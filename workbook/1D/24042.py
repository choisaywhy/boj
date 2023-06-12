import sys
from heapq import *

def solution(n,m,crosswalk):
    queue = [(0,1)]
    routes = [1e9]*(n+1)
    routes[1] = 0
    ans = 0

    for next, time in crosswalk[1]:
        routes[next] = time
        heappush(queue, (time, next, time))


    

    while queue:
        currtime, node, dist = heappop(queue)
        
        if routes[node] < dist:
            continue

        for next, time in crosswalk[node]:
            if routes[next] <= time + dist:
                continue










if __name__ == "__main__" :
    input = sys.stdin.readline
    n,m = map(int,input().split())
    crosswalk = [[] for _ in range(n+1)]
    for i in range(1,m+1):
        u,v = map(int,input().split())
        crosswalk[u].append((v,i))
        crosswalk[v].append((u,i))
    solution(n,m,crosswalk)