import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int,input().split())


def BFS(start, target):
    queue = deque([start])
    distance = [0]*100001

    while queue :
        node = queue.popleft()
        for next in [node-1, node+1, node*2] :
            if next == target :
                return distance[node] + 1
            if 0 <= next <= 100000 and not distance[next]:
                queue.append(next)
                distance[next] = distance[node] + 1

if N == K:
    print(0)
else :
    print(BFS(N,K))



import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int,input().split())


def BFS(start, target):
    queue = deque([(start,0)])
    visited = [False]*100001
    visited[start] = True

    while queue :
        node,time = queue.popleft()
        for next in [node-1, node+1, node*2] :
            if next == target :
                return time + 1
            if 0 <= next <= 100000 and not visited[next]:
                queue.append((next,time+1))
                visited[next] = True


if N == K:
    print(0)
else :
    print(BFS(N,K))
