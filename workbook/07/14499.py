import sys

def solution(N,M,x,y,K,maps,orders):
    directions = {1:[4,2,1,6,5,3,(0,1)], 
                2:[3,2,6,1,5,4,(0,-1)], 
                3:[5,1,3,4,6,2,(-1,0)], 
                4:[2,6,3,4,1,5,(1,0)]}
    dice = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    new_dice = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    
    for order in orders :
        dx, dy = directions[order][-1]
        nx, ny = dx + x, dy + y
        if 0 <= nx < N and 0 <= ny < M :
            for i in range(6) :
                new_dice[i+1] = dice[directions[order][i]]
            print(new_dice[1])
            if maps[nx][ny] == 0 :
                maps[nx][ny] = new_dice[6]
            else :
                new_dice[6] = maps[nx][ny]
                maps[nx][ny] = 0
                
            for _ in range(1,7) :
                dice[_] = new_dice[_]
            x, y = nx, ny



if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M, x, y, K = map(int, input().split())
    maps = [list(map(int,input().split())) for _ in range(N)]
    orders = list(map(int, input().split()))
    solution(N,M,x,y,K,maps,orders)


# import sys

# def solution(N,M,x,y,K,maps,orders):
#     directions = {1:[4,2,1,6,5,3,(0,1)], 
#                 2:[3,2,6,1,5,4,(0,-1)], 
#                 3:[5,1,3,4,6,2,(-1,0)], 
#                 4:[2,6,3,4,1,5,(1,0)]}
#     dice = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
#     new_dice = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    
#     for order in orders :
#         print('__________new turn__________',order)
#         dx, dy = directions[order][-1]
#         nx, ny = dx + x, dy + y
#         if 0 <= nx < N and 0 <= ny < M :
#             for i in range(6) :
#                 print('원래',directions[order][i],'가',i+1,'로 이동')
#                 new_dice[i+1] = dice[directions[order][i]]
#             print('brand new dice', new_dice)
#             print('answer',new_dice[1])

#             if maps[nx][ny] == 0 :
#                 print(new_dice[6],'가 지도로 복사')
#                 maps[nx][ny] = new_dice[6]
#             else :
#                 print(maps[nx][ny],'가 주사위 바닥면으로 복사')
#                 new_dice[6] = maps[nx][ny]
#                 maps[nx][ny] = 0
                
#             for _ in range(1,7) :
#                 dice[_] = new_dice[_]
#             x, y = nx, ny
#             print(maps, dice)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M, x, y, K = map(int, input().split())
#     maps = [list(map(int,input().split())) for _ in range(N)]
#     orders = list(map(int, input().split()))
#     solution(N,M,x,y,K,maps,orders)