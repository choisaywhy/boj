import sys
from collections import deque

input = sys.stdin.readline
directions = [(1,0),(-1,0),(0,1),(0,-1)]
M,N = map(int,input().split())


def BFS(box):
    queue = deque()
    # visitied = deque()
    day = 0 # 날짜 
    riped = 0 # 익은 토마토 개수 

    for x in range(N) :
        for y in range(M) :
            if box[x][y] == 1 : # 초기 1을 모두 queue에 넣음
                queue.append((x,y,day))
    while queue :
        nx,ny,day = queue.popleft()
        for d in directions :
            x, y = d[0] + nx, d[1] + ny
            if (0 <= x < N) and (0 <= y < M) : # 상하좌우 모든 방향 iter
                if not box[x][y]: # 방문하려는 노드가 익지 않은 토마토이고, 방문한적이 없으면
                    box[x][y] = 1
                    queue.append((x,y,day+1))
                    # visitied.append((x,y))
                    riped += 1 # 익은 토마토 개수
    return riped, day


box = []
raw = 0
for _ in range(N):
    box.append(list(map(int, input().split())))
    raw += box[_].count(0) # 익지 않은 토마토 개수 total

if not raw : # 익지 않은 토마토가 없으면 print 0
    print(0)
else : # 익지 않은 토마토가 있으면
    riped, day = BFS(box)
    if not (raw - riped) : # (초기 익지 않은 토마토 수) - (시간이 지나 익은 토마토 수) 가 0 이면 == 모든 익지 않은 토마토가 익었으면
        print(day)
    else : # 익지 않은 토마토가 존재하면
        print(-1)
    










# queue 사용 없이 진행
# import sys
# from collections import deque
# import copy


# directions = [(1,0),(-1,0),(0,-1),(0,1)]

# def BFS(box,next_box, start) :
#     x,y = start
#     change = 0
#     for d in directions :
#         nx, ny = x + d[0], y + d[1]
#         if (0 <= nx < N) and (0 <= ny < M) :
#             if box[nx][ny] == 0 and next_box[nx][ny] == 0:
#                 next_box[nx][ny] = 1
#                 change += 1
#     return next_box, change


# input = sys.stdin.readline
# M,N = map(int, input().split())
# box = []

# raw = 0
# for _ in range(N):
#     box.append(list(map(int, input().split())))
#     raw += box[_].count(0)
# next_box=copy.deepcopy(box)
# days = 0
# if not raw :
#     print(0)
# else :
#     while True :
#         days += 1
#         changes = []
#         for x in range(N):
#             for y in range(M):
#                 if box[x][y] == 1 :
#                     next_box, change = BFS(box,next_box, [x,y])
#                     changes.append(change)

#         box = copy.deepcopy(next_box)
#         raw -= sum(changes)
#         if not sum(changes) :
#             if raw :
#                 print(-1)
#                 break
#             else :
#                 print(days-1)
#                 break


    















# min을 활용하여 처리
# import sys
# from collections import deque

# directions = [(1,0),(-1,0),(0,-1),(0,1)]

# def BFS(box,start):
#     queue = deque([start])
#     visited = []
#     maximum = 0
#     raw = 0
#     while queue :
#         x,y = queue.popleft()
#         if [x,y] in visited :
#             continue

#         visited.append([x,y])
#         for d in directions :
#             nx, ny = d[0] + x, d[1] + y
#             if (0 <= nx < N) and (0 <= ny < M) :
#                 if box[nx][ny] > 0 :
#                     box[nx][ny] = min(box[nx][ny],box[x][y] + 1 )
#                 elif box[nx][ny] == 0 :
#                     raw += 1
#                     box[nx][ny] = box[x][y] + 1
#                 else :
#                     continue
#                 queue.append([nx,ny])
#                 if box[nx][ny] > maximum:
#                     maximum = box[nx][ny]
        
#     return box, maximum, raw
            

# input = sys.stdin.readline

# M, N = map(int,input().split())

# box = []
# raws = 0
# for i in range(N):
#     box.append(list(map(int,input().split())))
#     raws += box[i].count(0)
# # raw == 0 개수

# if not raws :
#     print(0)
# else :
#     for x in range(N):
#         for y in range(M):
#             if box[x][y] == 1:
#                 box,maximum, raw = BFS(box,[x,y])
#                 raws -= raw
#     if raws :
#         print(-1)
#     else :
#         print(maximum-1)




# import sys
# from collections import deque

# directions = [(1,0),(-1,0),(0,-1),(0,1)]

# def BFS(box,start):
#     queue = deque([start])
#     visited = []
#     while queue :
#         x,y = queue.popleft()
#         if [x,y] not in visited :
#             for d in directions :
#                 nx, ny = d
#                 nx, ny = nx + x, ny + y
#                 if (0 <= nx < N) and (0<= ny < M) :
#                     if box[nx][ny] > 0 :
#                         box[nx][ny] = min(box[nx][ny],box[x][y] + 1 )
#                         queue.append([nx,ny])
#                     elif box[nx][ny] == 0 :
#                         box[nx][ny] = box[x][y] + 1
#                         queue.append([nx,ny])
#             visited.append([x,y])
#     return box
            

# input = sys.stdin.readline

# M, N = map(int,input().split())

# box = []
# raw = False
# for i in range(N):
#     box.append(list(map(int,input().split())))
#     if 0 in box[i] :
#         raw = True
# if not raw :
#     print(0)

# for x in range(N):
#     for y in range(M):
#         if box[x][y] == 1:
#             box = BFS(box,[x,y])

# date = 0
# for x in range(N):
#     for y in range(M):
#         if box[x][y] > date :
#             date = box[x][y]
#         elif not box[x][y] :
#             raw = True
#             break
# if raw :
#     print(-1)
# else :
#     print(date-1)