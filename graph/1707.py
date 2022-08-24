import sys
from collections import deque

def BFS(graph,color,flag):
    queue = deque()
    visited = []

    queue.append(list(graph.keys())[0])

    while queue :
        node = queue.popleft()
        if node not in visited :
            visited.append(node)
            next = graph.pop(node)
            queue.extend(next)
            if color[node] == -1:
                color[node] = flag
            else :
                flag = color[node]
            flag = not flag
            for n in next :
                if color[n] == -1 :
                    color[n] = flag
                else :
                    if color[node] == color[n]:
                        return graph,color,flag,'NO'

                
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
        if result == 'NO':
            break
    print(result)

