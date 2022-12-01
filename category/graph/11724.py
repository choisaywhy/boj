import sys
from collections import deque

def DFS(graph):
    stack = deque()
    visited = []
    stack.append(list(graph.keys())[0])

    while stack :
        node = stack.pop()
        if node not in visited :
            visited.append(node)
            stack.extend(graph.pop(node))
    return graph


N, M = map(int, sys.stdin.readline().split())
graph = {}
for n in range(1,N+1):
    graph[n] = []
for _ in range(M):
    u,v = map(int, sys.stdin.readline().split())
    graph[u] += [v]
    graph[v] += [u]

count =0
while graph :
    graph=DFS(graph)
    count += 1

print(count)
