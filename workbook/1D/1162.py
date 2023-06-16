import sys
from heapq import *

def solution(n,m,k,roads):
    routes = [1e11]*(n+1)
    routes[1] = 0
    queue = [(0,1)] # cur dist, cur node

    while queue:
        dist, node = heappop(queue)
        






if __name__ == "__main__" :
    input = sys.stdin.readline
    n,m,k = map(int,input().split())
    roads = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        roads[u].append((v,w))
        roads[v].append((u,w))

    solution(n,m,k,roads)