# third trial with remembering x,y
# 2788ms -> 248ms vs deepcopy
# deepcopy is quite heavy
import sys

def solution(N,M,office,walls,cctv):
    directions = {1 : [[(0,1)], [(0,-1)], [(1,0)], [(-1,0)]],
                2 : [[(0,1),(0,-1)], [(1,0),(-1,0)]],
                3 : [[(-1,0),(0,1)], [(0,1),(1,0)], [(1,0),(0,-1)], [(0,-1),(-1,0)]],
                4 : [[(0,-1),(-1,0),(0,1)], [(0,-1),(1,0),(0,1)], [(1,0),(0,1),(-1,0)], [(1,0),(0,-1),(-1,0)]],
                5 : [[(0,1),(0,-1),(1,0),(-1,0)]]}

    def check_watched(x, y, direct):
        count = 0
        stack = []
        for d in direct:
            dx, dy = d
            now = (x,y)
            while True:
                nx,ny = now
                if not ( 0 <= nx + dx < N and 0 <= ny + dy < M ):
                    break
                if office[nx+dx][ny+dy] == 6:
                    break
                elif office[nx+dx][ny+dy] == 0:
                    office[nx+dx][ny+dy] = '#'
                    count += 1
                    stack.append((nx+dx, ny+dy))
                now = (nx+dx, ny+dy)

        return (count, stack)

    def DFS(depth, watched):
        nonlocal ans
        if depth == len(cctv):
            ans = min(ans, N*M - walls - len(cctv) - watched)
            return
        cctv_type, x, y = cctv[depth]
        for direct in directions[cctv_type]:
            count, stack = check_watched(x, y, direct)
            DFS(depth+1, watched+count)
            while stack :
                ex, ey = stack.pop()
                office[ex][ey] = 0
            

    ans = N*M
    DFS(0, 0)
    print(ans)



if __name__ == "__main__" :
    input = sys.stdin.readline
    N,M = map(int, input().split())
    office = []
    walls = 0
    cctv = []
    for x in range(N):
        office.append(list(map(int, input().split())))
        for y in range(M):
            if 1 <= office[x][y] <= 5:
                cctv.append((office[x][y], x, y))
            elif office[x][y] == 6:
                walls += 1

    solution(N,M,office,walls,cctv)



# second trial with deepcopy
# import sys
# from copy import deepcopy

# def solution(N,M,office,walls,cctv):
#     directions = {1 : [[(0,1)], [(0,-1)], [(1,0)], [(-1,0)]],
#                 2 : [[(0,1),(0,-1)], [(1,0),(-1,0)]],
#                 3 : [[(-1,0),(0,1)], [(0,1),(1,0)], [(1,0),(0,-1)], [(0,-1),(-1,0)]],
#                 4 : [[(0,-1),(-1,0),(0,1)], [(0,-1),(1,0),(0,1)], [(1,0),(0,1),(-1,0)], [(1,0),(0,-1),(-1,0)]],
#                 5 : [[(0,1),(0,-1),(1,0),(-1,0)]]}

#     def check_watched(x, y, direct, office):
#         count = 0
#         for d in direct:
#             dx, dy = d
#             now = (x,y)
#             while True:
#                 nx,ny = now
#                 if not ( 0 <= nx + dx < N and 0 <= ny + dy < M ):
#                     break
#                 if office[nx+dx][ny+dy] == 6:
#                     break
#                 elif office[nx+dx][ny+dy] == 0:
#                     office[nx+dx][ny+dy] = '#'
#                     count += 1
#                 now = (nx+dx, ny+dy)

#         return (office, count)

#     def DFS(depth, office, watched):
#         nonlocal ans
#         if depth == len(cctv):
#             ans = min(ans, N*M - walls - len(cctv) - watched)
#             return
#         cctv_type, x, y = cctv[depth]
#         copied = deepcopy(office)
#         for direct in directions[cctv_type]:
#             copied, count = check_watched(x, y, direct, copied)
#             DFS(depth+1, copied, watched+count)
#             copied = deepcopy(office)

#     ans = N*M
#     DFS(0, office, 0)
#     print(ans)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N,M = map(int, input().split())
#     office = []
#     walls = 0
#     cctv = []
#     for x in range(N):
#         office.append(list(map(int, input().split())))
#         for y in range(M):
#             if 1 <= office[x][y] <= 5:
#                 cctv.append((office[x][y], x, y))
#             elif office[x][y] == 6:
#                 walls += 1

#     solution(N,M,office,walls,cctv)




# debugging ver of second trial
# import sys
# from copy import deepcopy

# def solution(N,M,office,walls,cctv):
#     directions = {1 : [[(0,1)], [(0,-1)], [(1,0)], [(-1,0)]],
#                 2 : [[(0,1),(0,-1)], [(1,0),(-1,0)]],
#                 3 : [[(-1,0),(0,1)], [(0,1),(1,0)], [(1,0),(0,-1)], [(0,-1),(-1,0)]],
#                 4 : [[(0,-1),(-1,0),(0,1)], [(0,-1),(1,0),(0,1)], [(1,0),(0,1),(-1,0)], [(1,0),(0,-1),(-1,0)]],
#                 5 : [[(0,1),(0,-1),(1,0),(-1,0)]]}

#     def check_watched(x, y, direct, office):
#         count = 0
#         for d in direct:
#             dx, dy = d
#             now = (x,y)
#             while True:
#                 nx,ny = now
#                 print(nx,ny,'turn')
#                 if not ( 0 <= nx + dx < N and 0 <= ny + dy < M ):
#                     print('out of range break')
#                     break
#                 if office[nx+dx][ny+dy] == 6:
#                     print('met wall break')
#                     break
#                 elif office[nx+dx][ny+dy] == 0:
#                     print('void filled')
#                     office[nx+dx][ny+dy] = '#'
#                     count += 1
#                 now = (nx+dx, ny+dy)

#         print('fianl result is',office,count)
#         return (office, count)

#     def DFS(depth, office, watched):
#         nonlocal ans
#         if depth == len(cctv):
#             print('itered all depth', office)
#             ans = min(ans, N*M - walls - len(cctv) - watched)
#             print('ans updated', ans)
#             return
#         cctv_type, x, y = cctv[depth]
#         print(cctv_type,'type cctv',x,y,'turn')
#         copied = deepcopy(office)
#         print('searching in office',copied)
#         for direct in directions[cctv_type]:
#             print('itering in direct',direct)
#             copied, count = check_watched(x, y, direct, copied)
#             DFS(depth+1, copied, watched+count)
#             copied = deepcopy(office)

#     ans = N*M
#     DFS(0, office, 0)
#     print(ans)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N,M = map(int, input().split())
#     office = []
#     walls = 0
#     cctv = []
#     for x in range(N):
#         office.append(list(map(int, input().split())))
#         for y in range(M):
#             if 1 <= office[x][y] <= 5:
#                 cctv.append((office[x][y], x, y))
#             elif office[x][y] == 6:
#                 walls += 1

#     solution(N,M,office,walls,cctv)


# first trial
# import sys

# def solution(N,M,office,cctv):
#     directions = {1 : [[(0,1)], [(0,-1)], [(1,0)], [(-1,0)]],
#                   2 : [[(0,1),(0,-1)], [(1,0),(-1,0)]],
#                   3 : [[(-1,0),(0,1)], [(0,1),(1,0)], [(1,0),(0,-1)], [(0,-1),(-1,0)]],
#                   4 : [[(0,-1),(-1,0),(0,1)], [(0,-1),(1,0),(0,1)], [(1,0),(0,1),(-1,0)], [(1,0),(0,-1),(-1,0)]],
#                   5 : [[(0,1),(0,-1),(1,0),(-1,0)]]}
#     def check_visited(x,y,direct) :
#         for d in direct :
#             dx, dy = d
#             now = (x,y)
#             while True :
#                 nx, ny = now
#                 if not (0 <= nx + dx < N and 0 <= ny + dy < M) :
#                     break
#                 if office[nx+dx][ny+dy] == 6 :
#                     break
#                 elif office[nx+dx][ny+dy] == '#' or 1 <= office[nx+dx][ny+dy] <= 5 :
#                     now = (nx+dx, ny+dy)
#                 else : # 0인 경우
#                     office[nx+dx][ny+dy] = '#'
#                     now = (nx+dx, ny+dy)

#     for i in range(5,0,-1) :
#         if not cctv.get(i, False) :
#             continue
#         for v in cctv[i] :
#             x, y = v # i번째 cctv 좌표 x,y
#             max = 0
#             max_direct = []
#             for direct in directions[i] : # 하나의 방향 경우의 수
#                 count = 0

#                 for d in direct :
#                     dx, dy = d
#                     now = (x,y)
#                     while True :
#                         nx, ny = now
#                         if not (0 <= nx + dx < N and 0 <= ny + dy < M) :
#                             break
#                         if office[nx+dx][ny+dy] == 6 :
#                             break
#                         elif office[nx+dx][ny+dy] == '#' or 1 <= office[nx+dx][ny+dy] <= 5 :
#                             now = (nx+dx, ny+dy)
#                         else : # 0인 경우
#                             count += 1
#                             now = (nx+dx, ny+dy)
#                 if count >= max :
#                     max = count
#                     max_direct = direct

#             check_visited(x,y,max_direct) # updated office
        

#     ans = 0
#     for x in range(N) :
#         for y in range(M) :
#             if office[x][y] == 0 :
#                 ans += 1

#     print(ans)

# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M = map(int, input().split())
#     office = []
#     cctv = {}
#     for x in range(N):
#         office.append(list(map(int, input().split())))
#         for y in range(M):
#             if 1 <= office[x][y] <= 5 :
#                 cctv[office[x][y]] = cctv.get(office[x][y], []) + [(x,y)]

#     solution(N,M,office,cctv)




# debugging ver of the first trial
# import sys

# def solution(N,M,office,cctv):
#     directions = {1 : [[(0,1)], [(0,-1)], [(1,0)], [(-1,0)]],
#                   2 : [[(0,1),(0,-1)], [(1,0),(-1,0)]],
#                   3 : [[(-1,0),(0,1)], [(0,1),(1,0)], [(1,0),(0,-1)], [(0,-1),(-1,0)]],
#                   4 : [[(0,-1),(-1,0),(0,1)], [(0,-1),(1,0),(0,1)], [(1,0),(0,1),(-1,0)], [(1,0),(0,-1),(-1,0)]],
#                   5 : [[(0,1),(0,-1),(1,0),(-1,0)]]}
#     def check_visited(x,y,direct) :
#         for d in direct :
#             dx, dy = d
#             now = (x,y)
#             while True :
#                 nx, ny = now
#                 if not (0 <= nx + dx < N and 0 <= ny + dy < M) :
#                     break
#                 if office[nx+dx][ny+dy] == 6 :
#                     break
#                 elif office[nx+dx][ny+dy] == '#' or 1 <= office[nx+dx][ny+dy] <= 5 :
#                     now = (nx+dx, ny+dy)
#                 else : # 0인 경우
#                     office[nx+dx][ny+dy] = '#'
#                     now = (nx+dx, ny+dy)
#         print(office,'updated')

#     for i in range(5,0,-1) :
#         if not cctv.get(i, False) :
#             continue
#         for v in cctv[i] :
#             x, y = v # i번째 cctv 좌표 x,y
#             max = 0
#             max_direct = []
#             for direct in directions[i] : # 하나의 방향 경우의 수
#                 print(i,'type',x,y,'cctv turn in direct of ',direct)
#                 count = 0

#                 for d in direct :
#                     dx, dy = d
#                     now = (x,y)
#                     while True :
#                         nx, ny = now
#                         print('looking at',nx+dx,ny+dy)
#                         if not (0 <= nx + dx < N and 0 <= ny + dy < M) :
#                             print('end of office')
#                             break
#                         if office[nx+dx][ny+dy] == 6 :
#                             print('met wall')
#                             break
#                         elif office[nx+dx][ny+dy] == '#' or 1 <= office[nx+dx][ny+dy] <= 5 :
#                             print('met other cctv or already checked')
#                             now = (nx+dx, ny+dy)
#                         else : # 0인 경우
#                             # office[nx+dx][ny+dy] = '#'
#                             count += 1
#                             now = (nx+dx, ny+dy)
#                             print('met void',now,count,'updated')
#                 if count >= max :
#                     print('largest updated')
#                     max = count
#                     max_direct = direct

#             check_visited(x,y,max_direct) # updated office
#             print(i,'type cctv in',x,y,'maintains largest position on',max_direct,'number', max)
        
#             print('====비교의 대상은 여기서 분기===')

#     ans = 0
#     for x in range(N) :
#         for y in range(M) :
#             if office[x][y] == 0 :
#                 ans += 1

#     print(ans)

# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M = map(int, input().split())
#     office = []
#     cctv = {}
#     for x in range(N):
#         office.append(list(map(int, input().split())))
#         for y in range(M):
#             if 1 <= office[x][y] <= 5 :
#                 cctv[office[x][y]] = cctv.get(office[x][y], []) + [(x,y)]

#     solution(N,M,office,cctv)