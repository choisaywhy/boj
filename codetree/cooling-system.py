# https://www.codetree.ai/training-field/frequent-problems/problems/cooling-system/description?page=1&pageSize=20

import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())
airconditioners = [] # 에어컨 위치, 방향 x,y,s(0-3)
offices = [] # 사무실 좌표 x,y
cool = [[0]*n for _ in range(n)] # 시원함 정도
walls = [[-1]*n for _ in range(n)] # 벽이 없으면 -1, 벽이 있으면 방향(0,1)
time = 0
dx = [0,-1,0,1]
dy = [-1,0,1,0]

## input
for x in range(n):
    tmp = list(map(int,input().split()))
    for y in range(n):
        if tmp[y] == 1:
            offices.append((x,y))
        elif tmp[y] >= 2:
            airconditioners.append((x,y,tmp[y]-2))

for _ in range(m):
    x,y,s = map(int,input().split())
    walls[x][y] = s 



## declare methods

def able_togo(x,y,s): # 가려는 방향이 범위에 있는지, 벽이 있는지 확인
    if 0<= x+dx[s] <n and 0<= y+dy[s]<n and walls[x][y] != s:
        return True
    return False

def spread_coolair(x,y,s): # 각 에어컨에 대해 차가운 공기 뿌리기
    global cool
    visited = [[False]*n for _ in range(n)]
    visited[x+dx[s]][y+dy[s]] = True
    cool[x+dx[s]][y+dy[s]] += 5
    stack = [(x+dx[s],y+dy[s],5)]

    while stack:
        nx,ny,nc = stack.pop()

        if able_togo(nx,ny,s) and not visited[nx+dx[s]][ny+dy[s]]: # 정방향 칸 확인
            visited[nx+dx[s]][ny+dy[s]] = True
            cool[nx+dx[s]][ny+dy[s]] += nc - 1
            if nc - 1 > 1:
                stack.append((nx+dx[s],ny+dy[s],nc-1))
        
        for diff in [(s+1)%4, (s-1)%4]: # 45도 방향 칸 확인

            if able_togo(nx,ny,diff) and able_togo(nx+dx[diff], ny+dy[diff],s) and not visited[nx+dx[diff]+dx[s]][ny+dy[diff]+dy[s]]:
                visited[nx+dx[s]+dx[diff]][ny+dy[s]+dy[diff]] = True
                cool[nx+dx[s]+dx[diff]][ny+dy[s]+dy[diff]] += nc - 1
                if nc - 1 > 1:
                    stack.append((nx+dx[s]+dx[diff],ny+dy[s]+dy[diff],nc-1))
    
def mix_air(): # 공기 섞기
    global cool

    for x in range(n):
        for y in range(n): # 모든 좌표에 대해 
            for i in range(4): # 인접한 칸 확인
                if not able_togo(x,y,i): # 벽이 있는지, 범위 내에 있는지 확인
                    continue
                if cool[x][y] > cool[x+dx[i]][y+dy[i]]: # 현재 칸이 인접한 칸보다 시원한 경우
                    diff = (cool[x][y] - cool[x+dx[i]][y+dy[i]]) // 4
                    cool[x][y] -= diff
                    cool[x+dx[i]][y+dy[i]] += diff
    

def adjacent_walls(): # 외벽과 인접한 칸 시원함 -1
    global cool

    for x in range(n):
        for y in range(n):
            if 0 < x < n-1 and 0 < y < n-1:
                continue
            if cool[x][y] == 0:
                continue
            cool[x][y] -= 1

def check_office(): # 사무실의 모든 공간이 시원함 k를 만족하는지 확인
    for office in offices:
        x,y = office
        if cool[x][y] <k:
            return False
    return True


## main
while time < 100:
    for x,y,s in airconditioners:
        spread_coolair(x,y,s)
    mix_air()
    adjacent_walls()
    time += 1
    if check_office():
        break

print(-1 if time > 100 else time)