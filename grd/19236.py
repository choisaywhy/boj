import sys
from copy import deepcopy

def solution(fish,direct,board):
    directions = {1:(-1,0), 2:(-1,-1), 3:(0,-1), 4:(1,-1), 5:(1,0),
              6: (1,1), 7:(0,1), 8:(-1,1)} # (x+1) % 8 : 45 반시계 회전

    def check(f):
        nonlocal ans
        count = 0
        for idx in range(1,17):
            if f[idx] == []: # eaten
                count += idx
        if count > ans:
            ans = count
            
    def fish_move(b,f,d):
        for idx in range(1,17):
            if f[idx] == []: # already eaten
                continue
            x,y = f[idx]
            for i in range(8):
                tmp = (d[idx]+i)%8
                if tmp == 0:
                    tmp = 8
                dx, dy = directions[tmp]
                if not ( 0 <= x+dx < 4 and 0 <= y+dy < 4) or b[x+dx][y+dy] == -1:
                    continue
                next = b[x+dx][y+dy]
                f[idx], d[idx] = [x+dx, y+dy], tmp
                if next != 0:
                    f[next] = [x,y]
                b[x][y], b[x+dx][y+dy] = next, idx
                break
        return b,f,d
    
    def shark_move(sx,sy,sd,b): # 상어가 갈 수 있는 경로 return
        routes = []
        for i in range(1,4):
            dx, dy = directions[sd][0] * i, directions[sd][1] * i
            if not (0 <= sx + dx < 4 and 0 <= sy + dy < 4) or b[sx+dx][sy+dy] <= 0:
                continue
            routes.append((sx+dx,sy+dy))
        return routes

    def dfs(sx,sy,sd,b, f, d): # 상어 현재 위치, 방향
        b, f, d = fish_move(b, f, d)
        routes = shark_move(sx,sy,sd,b)

        if not routes:
            check(f)
            return
        
        b[sx][sy] = 0
        for r in routes:
            nx,ny = r
            next = b[nx][ny]
            f[next] = []
            b[nx][ny] = -1

            dfs(nx,ny,d[next],deepcopy(b), deepcopy(f), deepcopy(d))

            f[next] = [nx,ny]
            b[nx][ny] = next
        b[sx][sy] = -1
        
    ans = 0

    sx,sy,sd = 0,0,direct[board[0][0]]
    fish[board[0][0]] = []
    board[0][0] = -1

    dfs(sx,sy,sd,board, fish, direct)
    print(ans)

        

if __name__ == "__main__" :
    input = sys.stdin.readline

    fish = [[0,0] for _ in range(17)]
    direct = [0]*17
    board = [[0]*4 for _ in range(4)]

    for x in range(4):
        tmp = list(map(int,input().split()))
        for y in range(0,8,2):
            fish[tmp[y]] = [x,y//2]
            direct[tmp[y]] = tmp[y+1]
            board[x][y//2] = tmp[y]

    solution(fish,direct,board)



# 2nd trial debugging ver
# import sys
# from copy import deepcopy

# def solution(fish,direct,board):
#     directions = {1:(-1,0), 2:(-1,-1), 3:(0,-1), 4:(1,-1), 5:(1,0),
#               6: (1,1), 7:(0,1), 8:(-1,1)} # (x+1) % 8 : 45 반시계 회전

#     def check(f):
#         nonlocal ans
#         count = 0
#         for idx in range(1,17):
#             if f[idx] == []: # eaten
#                 count += idx
#         if count > ans:
#             ans = count
#         print(ans,'ans updated')
            
#     def fish_move(b,f,d):
#         for idx in range(1,17):
#             if f[idx] == []: # already eaten
#                 continue
#             x,y = f[idx]
#             for i in range(8):
#                 tmp = (d[idx]+i)%8
#                 if tmp == 0:
#                     tmp = 8
#                 dx, dy = directions[tmp]
#                 if not ( 0 <= x+dx < 4 and 0 <= y+dy < 4) or b[x+dx][y+dy] == -1:
#                     continue
#                 next = b[x+dx][y+dy]
#                 f[idx], d[idx] = [x+dx, y+dy], tmp
#                 if next != 0:
#                     f[next] = [x,y]
#                 b[x][y], b[x+dx][y+dy] = next, idx
#                 break
#         return b,f,d
    
#     def shark_move(sx,sy,sd,b): # 상어가 갈 수 있는 경로 return
#         routes = []
#         for i in range(1,4):
#             dx, dy = directions[sd][0] * i, directions[sd][1] * i
#             if not (0 <= sx + dx < 4 and 0 <= sy + dy < 4) or b[sx+dx][sy+dy] <= 0:
#                 continue
#             routes.append((sx+dx,sy+dy))
#         return routes

#     def dfs(sx,sy,sd,b, f, d): # 상어 현재 위치, 방향
#         b, f, d = fish_move(b, f, d)
#         routes = shark_move(sx,sy,sd,b)

#         print('board',b)
#         print('fish',f)
#         print('direct',d )

#         if not routes:
#             print('no routes no more to go')
#             check(f)
#             return
        
#         print('routes',routes)
#         b[sx][sy] = 0
#         for r in routes:
#             nx,ny = r
#             next = b[nx][ny]
#             f[next] = []
#             b[nx][ny] = -1

#             dfs(nx,ny,d[next],deepcopy(b), deepcopy(f), deepcopy(d))

#             f[next] = [nx,ny]
#             b[nx][ny] = next
#         b[sx][sy] = -1
        
#     ans = 0

#     sx,sy,sd = 0,0,direct[board[0][0]]
#     fish[board[0][0]] = []
#     board[0][0] = -1

#     dfs(sx,sy,sd,board, fish, direct)
#     print(ans)

        

# if __name__ == "__main__" :
#     input = sys.stdin.readline

#     fish = [[0,0] for _ in range(17)]
#     direct = [0]*17
#     board = [[0]*4 for _ in range(4)]

#     for x in range(4):
#         tmp = list(map(int,input().split()))
#         for y in range(0,8,2):
#             fish[tmp[y]] = [x,y//2]
#             direct[tmp[y]] = tmp[y+1]
#             board[x][y//2] = tmp[y]

#     solution(fish,direct,board)






# import sys
# from copy import deepcopy

# def solution(fish,direct,board):
#     directions = {1:(-1,0), 2:(-1,-1), 3:(0,-1), 4:(1,-1), 5:(1,0),
#               6: (1,1), 7:(0,1), 8:(-1,1)} # (x+1) % 8 : 45 반시계 회전

#     def check(f):
#         nonlocal ans
#         count = 0
#         for idx in range(1,17):
#             if f[idx] == []: # eaten
#                 count += idx
#         if count > ans:
#             ans = count
#         print(ans,'ans updated')
            
#     def fish_move(b,f,d):
#         for idx in range(1,17):
#             if f[idx] == []: # already eaten
#                 continue
#             x,y = f[idx]
#             for i in range(8):
#                 tmp = (d[idx]+i)%8
#                 if tmp == 0:
#                     tmp = 8
#                 dx, dy = directions[tmp]
#                 if not ( 0 <= x+dx < 4 and 0 <= y+dy < 4) or b[x+dx][y+dy] == -1:
#                     continue
#                 next = b[x+dx][y+dy]
#                 f[idx], d[idx] = [x+dx, y+dy], tmp
#                 if next != 0:
#                     f[next] = [x,y]
#                 b[x][y], b[x+dx][y+dy] = next, idx
#                 break
#         return b,f,d
    
#     def shark_move(sx,sy,sd,b): # 상어가 갈 수 있는 경로 return
#         routes = []
#         dx, dy = directions[sd]
#         while 0 <= sx + dx < 4 and 0 <= sy + dy < 4 and b[sx+dx][sy+dy] > 0:
#             routes.append((sx+dx,sy+dy))
#             sx, sy = sx + dx, sy + dy
#         return routes

#     def dfs(sx,sy,sd,b, f, d): # 상어 현재 위치, 방향
#         b, f, d = fish_move(b, f, d)
#         routes = shark_move(sx,sy,sd,b)

#         print('board',b)
#         print('fish',f)
#         print('direct',d )

#         if not routes:
#             print('no routes no more to go')
#             check(f)
#             return
        
#         b[sx][sy] = 0
#         for r in routes:
#             nx,ny = r
#             next = b[nx][ny]
#             f[next] = []
#             b[nx][ny] = -1

#             dfs(nx,ny,d[next],deepcopy(b), deepcopy(f), deepcopy(d))

#             f[next] = [nx,ny]
#             b[nx][ny] = next
#         b[sx][sy] = -1
        
#     ans = 0

#     sx,sy,sd = 0,0,direct[board[0][0]]
#     fish[board[0][0]] = []
#     board[0][0] = -1

#     dfs(sx,sy,sd,board, fish, direct)
#     print(ans)

        

# if __name__ == "__main__" :
#     input = sys.stdin.readline

#     fish = [[0,0] for _ in range(17)]
#     direct = [0]*17
#     board = [[0]*4 for _ in range(4)]

#     for x in range(4):
#         tmp = list(map(int,input().split()))
#         for y in range(0,8,2):
#             fish[tmp[y]] = [x,y//2]
#             direct[tmp[y]] = tmp[y+1]
#             board[x][y//2] = tmp[y]

#     solution(fish,direct,board)
