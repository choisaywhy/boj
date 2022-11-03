
# debugging
import sys
import heapq as hq
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
cave = [list(str(input()).strip()) for _ in range(R)] # R * C 크기
N = int(input())
directions = [(0,1),(0,-1),(1,0),(-1,0)]
turn = False # True : left -> right, False : right -> left

def BFS(cave, node) :
    queue = deque([node])
    visited = [ [False]*C for _ in range(R) ]

    while queue :
        x, y = queue.popleft()
        print(x,y,'살펴볼 차례')
        for dx, dy in directions :
            if 0 <= x + dx < R and 0 <= y + dy < C and cave[x + dx][y + dy] == 'x' and not visited[x + dx][y + dy] :
                if x + dx == R-1 : # 바닥에 닿은 경우
                    print('x',x,'dx',dx,'가 바닥에 닿음')
                    return True, cave
                visited[x + dx][y + dy] = True
                queue.append((x + dx, y + dy))
    return False, move(cave, visited) # 바닥에 닿지 않은 경우, 공중에 떠있는 모든 클러스터의 정보를 함께 넘김

def move(cave, cluster) :
    height = R
    for x in range(R-1,-1,-1) :
        for y in range(0,C) : # 아래 있는 클러스터를 먼저 이동시키기 위해 역순으로 실행
            if not cluster[x][y] :
                continue
            count = 0
            for i in range(x+1, R) :
                if cave[i][y] != '.' and not cluster[i][y]:
                    break
                count += 1
            height = min(count, height)
            print('다같이 움직여야 하는 ',height,x,y)
    print(cluster)
    for x in range(R) :
        for y in range(C):
            if cluster[x][y] :
                cave[x][y] = '.'
                cave[x+height][y] = 'x'

    return cave


for height in list(map(int, input().split())) :
    turn = not turn
    destroy_x = R-height

    if turn : # left -> right
        try :
            destroy_y = cave[R - height].index('x')
        except : # IndexError : 해당 height가 빈 줄일 경우 
            continue
    else : # right -> left
        try :
            destroy_y = C - (cave[R - height][::-1].index('x')+1)
        except : 
            continue

    cave[destroy_x][destroy_y] = '.' # x와 마주하면 해당 미네랄 파괴

    if destroy_x == 0 : # 위로 연결된 클러스터가 없는 경우
        continue
    
    print('막대기와 부딫힌 좌표는',destroy_x,destroy_y)

    ### 해당 좌표가 부서진 이후 처리가 중요함!!!!################ 221017
    for dx, dy in directions :
        if 0 <= destroy_x + dx < R and 0 <= destroy_y+ dy < C and cave[destroy_x + dx][destroy_y + dy] == 'x' :
            flag, cave = BFS(cave, (destroy_x + dx, destroy_y + dy))
    if flag : # 공중에 떠있지 않으면
        print('부서졌지만 문제 없음')
        continue
    else :
        print('부서짐')

for r in range(R):
    print("".join(cave[r]))

# 예제2번 5,4, 5,5 좌표 x 사라짐 오류,





