# 방법이 다르면 다른 경우의 수로 파악함

import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int,input().split())


def BFS(start, target):
    queue = deque([start]) # (위치, 시간)
    visited = [-1] * 100001
    dist = [0] * 100001
    visited[start] = 0
    dist[start] = 1
    

    while queue :
        node = queue.popleft()
        for next in [node-1, node+1, node*2] :
            if 0 <= next < 100001 :
                if visited[next] == -1:
                    queue.append(next)
                    visited[next] = visited[node] + 1
                    dist[next] = dist[node]
                else :
                    if visited[next] == visited[node] + 1 :
                        dist[next] += dist[node]

    print(visited[K], dist[K], sep= "\n")

if N == K :
    print(0,1, sep = "\n")
elif N > K :
    print(N-K,1, sep="\n")
else :
    BFS(N, K)
