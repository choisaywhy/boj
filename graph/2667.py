import sys
from collections import deque

directions = [(0,1),(0,-1),(1,0),(-1,0)]

def BFS(graph, start):
    queue = deque([start])
    visited = []
    while queue :
        nx,ny = queue.popleft()
        if [nx,ny] not in visited:
            for d in directions:
                x,y = d
                x,y = nx + x, ny + y
                if ( 0 <= x < N) and ( 0 <= y < N) :
                    if graph[x][y] :
                        queue.append([x,y])
            graph[nx][ny] = False
            visited.append([nx,ny])
    return len(visited), graph
        




input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(lambda x: True if x=="1" else False, str(input().rstrip()))))


town = []
for x in range(N):
    for y in range(N):
        if graph[x][y] :
            count = 0
            count, graph = BFS(graph,[x,y])
            town.append(count)
            

print(len(town))
for t in sorted(town) :
    print(t)