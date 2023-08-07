import sys
from collections import deque

def solution():
    n,m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    dx, dy = [-1,1,0,0],[0,0,1,-1]
    
    def bfs(x,y):
        queue = deque([(x,y)])
        visited = [[False]*m for _ in range(n)]
        visited[x][y] = True
        cheeze = 0

        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx,ny = x + dx[i], y + dy[i]

                if not( 0<= nx < n and 0<= ny <m) or visited[nx][ny]:
                    continue
                if board[nx][ny] == 0: # 테두리만 순회
                    queue.append((nx,ny))
                else: # 공기에 닿은 치즈
                    board[nx][ny] = 0
                    cheeze += 1
                visited[nx][ny] = True

        return cheeze
                    

    hours = 0
    cheeze = 0
    prev_cheeze = 0
    
    while True:

        cheeze = bfs(0,0)

        if not cheeze:
            break
        hours += 1    
        prev_cheeze = cheeze

    print(hours)
    print(prev_cheeze)


if __name__ == "__main__" :
    input = sys.stdin.readline
    
    solution()
