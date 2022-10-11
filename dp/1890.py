import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

def DFS(board, start) :
    stack = deque([start])
    visited = [[False]*N for _ in range(N)]
    visited[0][0] = True
    count = 0

    while stack :
        x, y = stack.popleft()
        visited[x][y] = True
        for next in [(x+board[x][y], y), (x, y+board[x][y])] :
            nx, ny = next
            if nx == N-1 and ny == N-1 :
                count += 1
                continue

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                stack.append((nx,ny))


    return count


board = list(list(map(int, input().split())) for _ in range(N))



print(DFS(board, (0,0)))