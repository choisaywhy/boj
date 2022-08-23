import sys
from collections import deque

def BFS(graph,color,flag):
    stack = deque()
    visited = []

    stack.append(list(graph.keys())[0])

    while stack :
        node = stack.pop()
        if node not in visited :
            print(node,'not visited')
            visited.append(node)
            stack.extend(graph.pop(node))
            flag = not flag
            color[node] = flag
            print(color)
        else :
            print(node,'visited')
            if color[node] == flag:
                print('겹침',color[node],flag)
                return graph,color,flag,'NO'
        print(node,graph, color)

                
    return graph,color,flag,'YES'


K = int(sys.stdin.readline())

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = {}
    for v in range(1,V+1):
        graph[v] = []
    for _ in range(E):
        u,v = map(int, sys.stdin.readline().split())
        graph[u] += [v]
        graph[v] += [u]
    color = {}
    for v in range(1,V+1):
        color[v] = -1
    flag = False
    while graph :
        graph,color,flag,result=BFS(graph,color,flag)
        print('end bfs')
        if result == 'NO':
            break
    print(result)

