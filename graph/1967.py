import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

def DFS(tree,node):
    stack = deque([node])
    visited = [False]*(n+1)
    length = (0,0)

    while stack :
        node, dist = stack.pop()
        if not visited[node] :
            visited[node] = True
            if dist > length[1] :
                length = (node, dist)
            for next in tree[node]:
                next_node, next_dist = next
                stack.append((next_node,dist+next_dist))
    return length



tree = {}

for _ in range(n-1) :
    nodes = list(map(int,input().split()))
    tree[nodes[0]] = tree.get(nodes[0], []) + [(nodes[1],nodes[2])]
    tree[nodes[1]] = tree.get(nodes[1], []) + [(nodes[0],nodes[2])]


node = 1
if n == 1 :
    print(0)
else :
    for _ in range(2):
        node,dist = DFS(tree,(node,0))

    print(dist)

