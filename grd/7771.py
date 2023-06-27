# 100이 있는 칸만 무조건 채우는 형태 출력
# sys.exit()로 강제 종료하는 형태
# 최단 거리 문제로 치환하여 bfs queue break으로 구현하는게 더 가독성 있을 것
import sys
from copy import deepcopy

def solution(attack, target):
    

    def dfs(depth, board,enable):

        if depth == 11:
            for x in range(10):
                print("".join(board[x]))
            sys.exit()

            return
        
        for x in range(10):
            for y in range(10):
                if board[x][y] == "#" or enable[x][y]:
                    continue

                for dx, dy in [(1,0),(0,1)]:
                    flag = True
                    tmpb = deepcopy(board)
                    tmpe = deepcopy(enable)

                    for i in range(ship[depth]): # 전함 크기 1 - 10 # if 2, 0,1 iter
                        nx, ny = dx * i + x, dy * i + y
                        if not( 0 <= nx < 10 and 0 <= ny < 10) or board[nx][ny] == "#" or enable[nx][ny]:
                            flag = False
                            break
                        tmpb[nx][ny] = "#"
                        for ex in [-1,0,1]:
                            for ey in [-1,0,1]:
                                if not( 0 <= nx+ex < 10 and 0 <= ny+ey < 10):
                                    continue
                                tmpe[nx+ex][ny+ey] = True

                    if flag:
                        dfs(depth+1, tmpb,tmpe)

    board = [['.']*10 for _ in range(10)]
    enable = [[False]*10 for _ in range(10)]
    ship = {2:1, 3: 1, 4:1, 5:2, 6:2, 7:2, 8:3, 9:3, 10:4}

    tx, ty = target
    board[tx][ty] = "#"
    for ex in [-1,0,1]:
        for ey in [-1,0,1]:
            if not( 0 <= tx+ex < 10 and 0 <= ty+ey < 10):
                continue
            enable[tx+ex][ty+ey] = True
    dfs(2, board,enable)


if __name__ == "__main__" :
    input = sys.stdin.readline

    attack = []
    target = (0,0)
    for x in range(10):
        attack.append(list(map(int, input().split())))
        for y in range(10):
            if attack[x][y] == 100:
                target = (x,y)
                break
    solution(attack, target)

    




# with enable check
# dfs로 모든 경우의수 구하기
# 무한 루프 빠짐
# import sys
# from copy import deepcopy

# def solution(attack):
    
#     def check_board(board):
#         pass


#     def dfs(depth, board,enable, score):
#         nonlocal ans, count
#         print('depth',depth,'score',score)
#         print('board',board)
#         print('enable',enable)
#         print('turn')
#         if depth == 11:
#             print('no more to go')
#             if score > count:
#                 count = score
#                 ans = board
#                 print('brand new ans',ans)
#             return
        
#         for x in range(10):
#             for y in range(10):
#                 if board[x][y] == "#" or enable[x][y]:
#                     continue
#                 print(x,y,'turn')
#                 tmpb = deepcopy(board)
#                 tmpe = deepcopy(enable)
#                 tmps = attack[x][y]
#                 for dx, dy in [(1,0),(0,1)]:
#                     flag = True

#                     for i in range(ship[depth]): # 전함 크기 1 - 10 # if 2, 0,1 iter
#                         nx, ny = dx * i + x, dy * i + y
#                         if not( 0 <= nx < 10 and 0 <= ny < 10) or tmpb[nx][ny] == "#" or tmpe[nx][ny]:
#                             flag = False
#                             print(nx,ny,'enable')
#                             break
#                         tmpb[nx][ny] = "#"
#                         tmpe[nx][ny] = True
#                         tmps = max(tmps, attack[nx][ny])
#                         for ex in [-1,0,1]:
#                             for ey in [-1,0,1]:
#                                 if not( 0 <= nx+ex < 10 and 0 <= ny+ey < 10):
#                                     continue
#                                 if attack[nx+ex][ny+ey] >= count:
#                                     return
#                                 tmpe[nx+ex][ny+ey] = True

#                     if flag:
#                         dfs(depth+1, tmpb,tmpe, max(tmps,score))

#     board = [['.']*10 for _ in range(10)]
#     enable = [[False]*10 for _ in range(10)]
#     ship = {1:1, 2:1, 3: 1, 4:1, 5:2, 6:2, 7:2, 8:3, 9:3, 10:4}
#     count = 0
#     ans = []

#     dfs(1, board,enable, 0)
            
#     print(ans)




# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     attack = [list(map(int, input().split())) for _ in range(10)]
#     solution(attack)

    