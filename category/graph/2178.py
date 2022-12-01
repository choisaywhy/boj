import sys
from collections import deque

input = sys.stdin.readline
directions = [(1,0),(-1,0),(0,1),(0,-1)]
maps = []
N = int(input())
for _ in range(N):
    maps.append(list(map(int, input().split())))

def islandBFS(maps,num):
    queue = deque()

    for x in range(N):
        for y in range(N):
            if maps[x][y] != 1:
                continue
            queue.append((x,y))
            maps[x][y] = num

            while queue:
                x,y = queue.popleft()
                
                for d in directions:
                    nx, ny = d[0] + x, d[1] + y
                    if (0 <= nx < N) and (0 <= ny < N) and maps[nx][ny] == 1:
                        queue.append((nx,ny))
                        maps[nx][ny] = num

            num += 1

    return maps, num
    


def bridgeBFS(maps,num) :
    queue = deque()
    visited = [[False]*N for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if maps[x][y] != num :
                continue
            queue.append((x,y,0))
            visited[x][y] = True

    while queue:
        x,y,dist = queue.popleft()
        # print(x,y,dist)
        for d in directions:
            nx, ny = d[0] + x, d[1] + y
            if (0 <= nx < N) and (0 <= ny < N) and not visited[nx][ny] :
                if not maps[nx][ny]: # 0 이면
                    queue.append((nx,ny,dist+1))
                    visited[nx][ny] = True          
                else: # 최단 거리를 가진 island 번호, 최단 거리 return
                    return dist

maps,num = islandBFS(maps,2)

bridge = []
for i in range(2,num) :
    bridge.append(bridgeBFS(maps,i))
print(min(bridge))


# 시간 초과
# islandBFS 가 BFS 중복 호출로 시간 잡아먹음
# maps를 활용한 visited 체크와 전체 maps iter을 내부로 돌리니, maps를 전체 한번만 돌아도 됨

# import sys
# from collections import deque

# input = sys.stdin.readline
# directions = [(1,0),(-1,0),(0,1),(0,-1)]
# maps = []
# N = int(input())
# for _ in range(N):
#     maps.append(list(map(int, input().split())))

# def islandBFS(maps,start,num):
#     queue = deque([start])

#     while queue:
#         x,y = queue.popleft()
#         maps[x][y] = num
        
#         for d in directions:
#             nx, ny = d[0] + x, d[1] + y
#             if (0 <= nx < N) and (0 <= ny < N) and maps[nx][ny] == 1:
#                 queue.append((nx,ny))
                
#     return maps
    


# def bridgeBFS(maps,num) :
#     queue = deque()
#     visited = deque()

#     for x in range(N):
#         for y in range(N):
#             if maps[x][y] == num :
#                 queue.append((x,y,0))
#                 visited.append((x,y))

#     while queue:
#         x,y,dist = queue.popleft()
#         print('exploring',x,y,dist)
#         for d in directions:
#             nx, ny = d[0] + x, d[1] + y
#             if (0 <= nx < N) and (0 <= ny < N) and (nx,ny) not in visited :
#                 if not maps[nx][ny]: # 0 이면
#                     queue.append((nx,ny,dist+1))
#                     visited.append((nx,ny))           
#                 else: # 최단 거리를 가진 island 번호, 최단 거리 return
#                     return dist

# num = 2
# for x in range(N):
#     for y in range(N):
#         if maps[x][y] == 1:
#             maps = islandBFS(maps,(x,y), num)
#             num += 1
# bridge = []
# for i in range(2,num) :
#     print(i)
#     dist= bridgeBFS(maps,i)
#     bridge.append(dist)

# print(min(bridge))