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

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    array = list(map(int, input().split()))
    graph = {}
    for i in range(1,N+1):
        graph[i] = []
    for i in range(N):
        graph[i+1] += [array[i]]
        graph[array[i]] += [i+1]
    count = 0
    while graph :
        graph=DFS(graph)
        count += 1

    print(count)



