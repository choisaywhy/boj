import sys
from collections import deque

input = sys.stdin.readline
N,M = map(int, input().split())
directions = [(1,0),(-1,0),(0,1),(0,-1)]
maze = []

def BFS(maze,start) :
    queue = deque([start])
    visited = deque()

    while queue :
        x,y,dist = queue.popleft()
        if (x,y) == (N-1,M-1) :
            return dist
        if (x,y) not in visited :
            visited.append((x,y))
            for d in directions:
                nx, ny = d[0] + x, d[1] + y
                
                if (0 <= nx < N) and (0 <= ny < M) and maze[nx][ny] :
                    queue.append((nx,ny,dist+1))
                    


for _ in range(N):
    maze.append(list(map(lambda x : True if x == "1" else False, str(input().strip()))))

print(BFS(maze, (0,0,1)))

