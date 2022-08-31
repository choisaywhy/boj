import sys
from collections import deque

input = sys.stdin.readline
directions = ((1,0),(-1,0),(0,1),(0,-1))
R, C = map(int,input().split())

def lakeBFS(lake) :
    stack = deque()
    visited = [[False]*C for _ in range(R)]
    for x in range(R) :
        for y in range(C) :
            if lake[x][y] != "X" :
                stack.append((x,y))
                visited[x][y] = True
    
    while stack :
        x,y = stack.popleft()
        for direction in directions :
            nx, ny = x + direction[0], y + direction[1]
            if (0 <= nx < R) and (0 <= ny < C) and not visited[nx][ny] and lake[nx][ny] == 'X':
                lake[nx][ny] = '.'
                visited[nx][ny] = True                    
    return lake
    


def swanBFS(lake, start, target) :
    stack = deque([start])
    visited = [[False]*C for _ in range(R)]
    visited[start[0]][start[1]] = True

    while stack :
        x,y = stack.popleft()
        for direction in directions :
            nx, ny = x + direction[0], y + direction[1]
            if (0 <= nx < R) and (0 <= ny < C) and not visited[nx][ny] and lake[nx][ny] != 'X' :
                if (nx,ny) == target :
                    return True
                else :
                    visited[nx][ny] = True
                    stack.append((nx,ny))
    return False

        


lake = [] # . : 이동 가능, X : 이동 불가
swan = [] # 백조의 정보 swan[1] : (x,y) ... 
for i in range(R) :
    lake.append(list(map(str,input().strip())))
    for j in range(C) :
        if lake[i][j] == "L" :
            swan.append((i,j))

days = 0

while not swanBFS(lake, swan[0], swan[1]) :
    days += 1
    lake = lakeBFS(lake)
    # print('lake of day',days)
    # print(lake)
    
print(days)


# 백조가 입력 한 줄에 있는 경우
# 백조의 위치 또한 물이기 때문에 lake에 포함해주어야함