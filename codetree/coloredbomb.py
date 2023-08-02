import sys
import copy
from collections import deque

def solution():
    n,m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    answer = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def gravity():
        nonlocal board

        for y in range(n):
            tmp = [-2]*n
            idx = n-1 # 기준 행 idx
            for x in range(n-1,-1,-1):
                if board[x][y] == -1:
                    tmp[x] = -1
                    idx = x - 1
                elif board[x][y] > -1:
                    tmp[idx] = board[x][y]
                    idx -= 1

            for x in range(n):
                board[x][y] = tmp[x]

    def rotate():
        nonlocal board
        rotated = [[0]*n for _ in range(n)]

        for x in range(n):
            for y in range(n):
                rotated[n-1-y][x] = board[x][y]
        
        board = rotated

    def bfs(x,y):

        queue = deque([(x,y)]) # 현재 좌표, 폭탄 수, 빨간색 폭탄 수, 기준점, 경로
        color = board[x][y]
        bomb,red = 1, 0 if board[x][y] != 0 else 1
        msx,msy = -1,n
        routes = [(x,y)]
        while queue:
            x,y = queue.popleft()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if not(0<=nx<n and 0<= ny <n) or (nx,ny) in routes or board[nx][ny] == -1: # 범위, 방문, 돌 체크
                    continue
                if not (board[nx][ny] == 0 or board[nx][ny] == color): # 색깔 체크
                    continue
                if board[nx][ny] == 0 : # red
                    red += 1
                    bomb += 1
                else:
                    bomb += 1
                    if (nx, -ny) > (msx, -msy): # 빨강이 아닌 폭탄 기준점 갱신
                        msx, msy = nx, ny
                queue.append((nx,ny))
                routes.append((nx,ny))
                color = board[nx][ny] if color == 0 else color # 빨간색인 경우 다른 색 하나 추가

        return bomb, red, msx, msy, routes

    def select():
        nonlocal answer 
        nonlocal board

        ans = (0,400,-1,n)
        ans_routes = []
        for x in range(n):
            for y in range(n):
                if board[x][y] >= 0:
                    bomb, red, msx, msy, routes = bfs(x,y)
                    if bomb < 2 or bomb == red: # 2개 이상 안되거나 모두 빨간색인 경우
                        continue
                    if ans < (bomb, -red, msx, -msy):
                        ans = (bomb, -red, msx, -msy)
                        ans_routes = routes

        for r in ans_routes:
            board[r[0]][r[1]] = -2 # 없어진 폭탄 지우기 / 빈공간 -2
        
        if ans[0] == 0: # 더 이상 터질 폭탄 없음
            return False
        answer += (ans[0]**2)
        return True

    ### 메인 실행
    while True:
        if not select():
            break
        gravity()
        rotate()
        gravity()

    print(answer)

if __name__ == "__main__" :
    input = sys.stdin.readline
    solution()
