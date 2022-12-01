import sys
from collections import deque

def DFS(graph, V):
    stack = deque()
    visited = []

    stack.append(V)

    while stack :
        node = stack.pop()
        if node not in visited :
            visited.append(node)
            print(node, end=" ")
            stack.extend(sorted(graph[node],reverse=True))
    return


def BFS(graph, V):
    queue = deque()
    visited = []

    queue.append(V)

    while queue :
        node = queue.popleft()
        if node not in visited :
            visited.append(node)
            print(node, end=" ")
            queue.extend(sorted(graph[node]))
    return visited


N, M, V = map(int, sys.stdin.readline().split())
graph = {}
for n in range(1,N+1):
    graph[n] = []
for _ in range(M):
    x,y = map(int, sys.stdin.readline().split())
    graph[x] = graph.get(x,[]) + [y]
    graph[y] = graph.get(y,[]) + [x]

DFS(graph, V)
print()
BFS(graph, V)