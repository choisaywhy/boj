import sys

def solution(gears, turns):
    target = [0,0,0,0]

    for turn in turns:
        stack = [(turn[0] - 1, turn[1])]
        visited = [False]*4
        while stack:
            gear, direct = stack.pop()
            visited[gear] = direct
            if gear + 1 < 4: # 오른쪽에 다른 기어가 있는 경우
                if not visited[gear+1]:
                    pole = gears[gear][(target[gear]+2)%8] # 현재 상태의 맞닿는 극 정보
                    poleleft = gears[gear+1][(target[gear+1]+6)%8]
                    if pole != poleleft:
                        stack.append((gear+1, 1 if direct == -1 else -1))

            if gear - 1 > -1: # 왼쪽에 다른 기어가 있는 경우
                if not visited[gear-1]:
                    pole = gears[gear][(target[gear]+6)%8] # 현재 상태의 맞닿는 극 정보
                    poleright = gears[gear-1][(target[gear-1]+2)%8]
                    if pole != poleright:
                        stack.append((gear-1, 1 if direct == -1 else -1))

        for i in range(4):
            if not visited[i]:
                continue
            if visited[i] == 1:
                target[i] = (target[i]+7)%8
            elif visited[i] == -1:
                target[i] = (target[i]+1)%8
            
        
    ans = 0
    for i in range(4):
        if gears[i][target[i]] == 0:
            continue
        ans += 2**(i)
    
    print(ans)




if __name__ == "__main__" :
    input = sys.stdin.readline
    gears = [list(map(int, input().strip())) for _ in range(4)]
    K = int(input())
    turns = []
    for _ in range(K):
        turns.append(tuple(map(int, input().split())))
    solution(gears, turns)


# debugging ver
# import sys

# def solution(gears, turns):
#     target = [0,0,0,0]

#     for turn in turns:
#         print(turn[0],'회전')
#         stack = [(turn[0] - 1, turn[1])]
#         visited = [False]*4
#         while stack:
#             gear, direct = stack.pop()
#             visited[gear] = direct
#             print(gear,'번째 기어',direct,'로 회전')
#             if gear + 1 < 4: # 오른쪽에 다른 기어가 있는 경우
#                 print('오른쪽에 기어 있음')
#                 if not visited[gear+1]:
#                     pole = gears[gear][(target[gear]+2)%8] # 현재 상태의 맞닿는 극 정보
#                     poleleft = gears[gear+1][(target[gear+1]+6)%8]
#                     if pole != poleleft:
#                         print('회전하기 전 두 극 다름',pole,poleleft)
#                         stack.append((gear+1, 1 if direct == -1 else -1))
#                         print(stack,'stack updated')

#             if gear - 1 > -1: # 왼쪽에 다른 기어가 있는 경우
#                 print('왼쪽에 기어 있음')
#                 if not visited[gear-1]:
#                     pole = gears[gear][(target[gear]+6)%8] # 현재 상태의 맞닿는 극 정보
#                     poleright = gears[gear-1][(target[gear-1]+2)%8]
#                     print((target[gear]+6)%8, target[gear])
#                     if pole != poleright:
#                         print('회전하기 전 두 극 다름',pole,poleright)
#                         stack.append((gear-1, 1 if direct == -1 else -1))
#                         print(stack,'stack updated')

#         print('극 회전 시작')
#         for i in range(4):
#             if not visited[i]:
#                 continue
#             if visited[i] == 1:
#                 target[i] = (target[i]+7)%8
#             elif visited[i] == -1:
#                 target[i] = (target[i]+1)%8
            
#         print('최종 업데이트 된 극',target)
        
#     print(target)
#     ans = 0
#     for i in range(4):
#         if gears[i][target[i]] == 0:
#             continue
#         ans += 2**(i)
    
#     print(ans)




# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     gears = [list(map(int, input().strip())) for _ in range(4)]
#     K = int(input())
#     turns = []
#     for _ in range(K):
#         turns.append(tuple(map(int, input().split())))
#     solution(gears, turns)



# 문제 이해 오류
# import sys

# def solution(gears, turns):
#     target = [gears[0][0], gears[1][0], gears[2][0], gears[3][0]]
#     # 왼쪽 0, 오른쪽 1
#     def rotation(gear, direct,lr, pole): # gear의 극 정보가 pole이 될때까지 돌리기
#         direct_num = 1
#         direct_lr = 6
#         if direct == -1:
#             direct_num = 7
#         if lr == 1:
#             direct_lr = 2
        
#         t = target[gear]

#         while True:
#             if pole == gears[gear][(t+direct_lr)%8]:
#                 break
#             else:
#                 t = (t+direct_num)%8
        
#         target[gear] = t


#     for turn in turns:
#         gear, direct = turn[0] - 1, turn[1]
#         if direct == 1: # 시계방향 회전
#             target[gear] = (target[gear] + 7) % 8
#         else:
#             target[gear] = (target[gear] + 1) % 8   

#         if gear + 1 < 4: # 오른쪽에 다른 기어가 있는 경우
#             pole = gears[gear][(target[gear]+2)%8] # 현재 상태의 맞닿는 극 정보
#             poleleft = gears[gear+1][(target[gear]+6)%8]
#             if pole == poleleft:
#                 continue
#             rotation(gear+1, direct,0, pole)

#         if gear - 1 > -1: # 왼쪽에 다른 기어가 있는 경우
#             pole = gears[gear][(target[gear]+6)%8] # 현재 상태의 맞닿는 극 정보
#             poleright = gears[gear-1][(target[gear]+2)%8]
#             if pole == poleright:
#                 continue
#             rotation(gear-1, direct,1, pole)
    
#     print(target)
#     ans = 0
#     for i in range(4):
#         if gears[i][target[i]] == 0:
#             continue
#         ans += 2**(i)
    
#     print(ans)




# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     gears = [list(map(int, input().strip())) for _ in range(4)]
#     K = int(input())
#     turns = []
#     for _ in range(K):
#         turns.append(tuple(map(int, input().split())))
#     solution(gears, turns)