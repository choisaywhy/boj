import sys
from copy import deepcopy

def solution(N,M,office,cctv):
    directions = {1 : [[0], [1], [2], [3]],
                  2 : [[1,3], [0,2]],
                  3 : [[0,1], [1,2], [2,3], [3,0]],
                  4 : [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
                  5 : [[0,1,2,3]]}
    
    points = [(-1,0),(0,1),(1,0),(0,-1)]
    
    def check_visited(temp_office,x,y,direct) :
        for d in direct :
            dx, dy = points[d][0], points[d][1]
            while True :
                x += dx
                y += dy
                if not (0 <= x < N and 0 <= y < M) :
                    break
                if temp_office[x][y] == 6 :
                    break
                elif temp_office[x][y] == 0 :
                    temp_office[x][y] = '#'

    ans = N*M

    def dfs(depth, office) :
        nonlocal ans
        if depth == len(cctv) :
            count = 0
            for i in range(N) :
                count += office[i].count(0)
            ans = min(ans, count)
            return
        
        
        temp_office = deepcopy(office)
        cctv_type, x, y = cctv[depth]
        for direct in directions[cctv_type] :
            check_visited(temp_office, x,y,direct)
            dfs(depth+1, temp_office)
            temp_office = deepcopy(office)
    
    dfs(0, office)
    print(ans)



if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    office = []
    cctv = []
    cctv_num = 0
    for x in range(N):
        office.append(list(map(int, input().split())))
        for y in range(M):
            if 1 <= office[x][y] <= 5 :
                cctv.append((office[x][y], x, y))

    solution(N,M,office,cctv)




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