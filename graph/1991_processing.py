import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = {}

for _ in range(N):
    nodes = list(map(str, input().strip().split()))
    graph[nodes[0]] = nodes[1:]


def preorder(graph,root):
    stack = deque([root])
    visited = deque()

    while stack :
        node = stack.pop()
        if node == ".":
            continue
        if node not in visited :
            visited.append(node)
            stack.extend(graph[node])

print(preorder(graph,root))