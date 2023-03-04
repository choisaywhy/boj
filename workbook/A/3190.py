import sys
from collections import deque

def solution(n, k, maps, l, shift):
    directions = [(0,1),(1,0),(0,-1),(-1,0)] # 동남서북 0,1,2,3
    cur_dir = 0 # 현재 방향 index of directions
    second = 1
    snake = deque([(0,0)]) # 뱀 좌표 순서대로 (머리, ... , 꼬리)
    maps[0][0] = 's' # 지도 표기 : 뱀-'s', 빈공간-0, 사과-'a'

    while True :
    
        dx, dy = directions[cur_dir] # 방향 좌표
        hx, hy = snake[0] # 뱀 머리 좌표
        tx, ty = snake[-1] # 뱀 꼬리 좌표
        nx, ny = dx + hx, dy + hy # 머리가 이동 할 좌표

        # 종료 조건
        if not (0 <= nx < n and 0 <= ny < n) :# 벽을 만난 경우
            break
        if maps[nx][ny] == 's' : # 자기 자신을 만난 경우
            break
        
        # 머리 길이 늘리기
        if maps[nx][ny] == 0 : # 사과가 없다면 꼬리 줄이기
            maps[tx][ty] = 0
            snake.pop()      
        snake.appendleft((nx,ny)) # 머리 갱신
        maps[nx][ny] = 's'

        # 방향 바꾸기
        if shift.get(second, False):
            if shift[second] == "D":
                cur_dir = (cur_dir+1) % 4
            elif shift[second] == "L":
                cur_dir = (cur_dir-1) % 4

        second += 1

    print(second)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    k = int(input())
    maps = [[0]*n for _ in range(n)] 
    for _ in range(k):
        ax, ay = map(int, input().split())
        maps[ax-1][ay-1] = 'a'
    l = int(input())
    shift = {} # 방향 전환 {시간:방향}
    for _ in range(l):
        x, c = map(str, input().strip().split())
        shift[int(x)] = c
    
    solution(n, k, maps, l, shift)



# debugging ver
# import sys
# from collections import deque

# def solution(n, k, maps, l, shift):
#     directions = [(0,1),(1,0),(0,-1),(-1,0)] # 동남서북 0,1,2,3
#     cur_dir = 0 # directions index
#     second = 1
#     snake = deque([(0,0)])
#     maps[0][0] = 1
#     while True :
#         print(second,'time','to direct',cur_dir)
#         dx, dy = directions[cur_dir]
#         hx, hy = snake[0]
#         tx, ty = snake[-1]
#         nx, ny = dx + hx, dy + hy
#         if not (0 <= nx < n and 0 <= ny < n) :# 벽을 만난 경우
#             print('벽이랑 만남 ㅅㄱ')
#             break
#         if maps[nx][ny] == 1 : # 자기 자신을 만난 경우
#             print('나랑 만남 ㅅㄱ')
#             break
        
#         # 머리 길이 늘리기
#         if maps[nx][ny] == 'apple' :
#             print('사과 있음')
#         elif maps[nx][ny] == 0 : # 사과가 없다면 꼬리 줄이기
#             print('사과 없음')
#             maps[tx][ty] = 0
#             snake.pop()      
#         snake.appendleft((nx,ny))
#         maps[nx][ny] = 1

#         if shift.get(second, False):
#             print('다음부터 방향 바뀜')
#             if shift[second] == "D":
#                 print('오른쪽으로')
#                 cur_dir += 1
#                 if cur_dir == 4 :
#                     cur_dir = 0  
#             elif shift[second] == "L":
#                 print('왼쪽으로')
#                 cur_dir -= 1
#                 if cur_dir == -1 :
#                     cur_dir = 4
#             print('updated direct')

#         print('head',snake[0], 'tail',snake[-1],'direct', cur_dir)

#         second += 1

#     print(second)


# if __name__ == "__main__":
#     input = sys.stdin.readline
#     n = int(input())
#     k = int(input())
#     maps = [[0]*n for _ in range(n)] 
#     for _ in range(k):
#         ax, ay = map(int, input().split())
#         maps[ax-1][ay-1] = 'apple'
#     l = int(input())
#     shift = {}
#     for _ in range(l):
#         x, c = map(str, input().split())
#         shift[int(x)] = c
    
#     solution(n, k, maps, l, shift)