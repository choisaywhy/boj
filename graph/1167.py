import sys
from collections import deque

input = sys.stdin.readline

def DFS(tree,node):
    stack = deque([node])
    visited = [False]*(len(tree)+1)
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




V = int(input())
tree = {}

for _ in range(V) :
    nodes = list(map(int,input().split()))[:-1]
    tree[nodes[0]] = []
    for node in range(1,len(nodes),2) :
        tree[nodes[0]] += [(nodes[node],nodes[node+1])]

node = 1
for _ in range(2):
    node,dist = DFS(tree,(node,0))

print(dist)






# stack으로 구현
# import sys
# from collections import deque

# input = sys.stdin.readline

# def DFS(tree,node):
#     stack = deque([node])
#     visited = [False]*(len(tree)+1)
#     length = 0

#     while stack :
#         node, dist = stack.pop()
#         if not visited[node] :
#             visited[node] = True
#             if dist > length :
#                 length = dist
#             for next in tree[node]:
#                 next_node, next_dist = next
#                 stack.append((next_node,dist+next_dist))
#     return length




# V = int(input())
# tree = {}

# for _ in range(V) :
#     nodes = list(map(int,input().split()))[:-1]
#     tree[nodes[0]] = []
#     for node in range(1,len(nodes),2) :
#         tree[nodes[0]] += [(nodes[node],nodes[node+1])]

# length = []

# for v in range(1,V+1):
#     length.append(DFS(tree,(v,0)))
# print(max(length))

