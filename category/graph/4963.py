import sys
from collections import deque

dx = [-1,0,1]
dy = [-1,0,1]

def BFS(graph, start):
    queue = deque([start])
    visited = []

    while queue :
        nx,ny = queue.popleft()
        if [nx,ny] not in visited:
            for x in dx :
                for y in dy :
                    gx,gy = nx + x, ny + y
                    if ( 0 <= gx < len(graph)) and ( 0 <= gy < len(graph[0])) :
                        if graph[gx][gy] :
                            queue.append([gx,gy])
            graph[nx][ny] = False
            visited.append([nx,ny])
    return graph
        


input = sys.stdin.readline
W ,H = 1,1

while True :
    W, H = map(int,input().split())
    if not W or not H :
        break
    graph = []
    for _ in range(H):
        graph.append(list(map(lambda x: False if not x else True, list(map(int,input().split())) )))

    
    island = 0
    for x in range(H):
        for y in range(W):
            if graph[x][y] :
                graph = BFS(graph,[x,y])
                island += 1
    print(island)