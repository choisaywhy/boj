# 3rd trial
# 지훈이 자체가 불에 타고 있는 경우 고려 안함 -> 지훈 좌표 "F"면 continue 구문 추가
import sys
from collections import deque

def solution(R, C, maze, jh, fire) :
    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    def flame(fire) :
        new_fire = []
        while fire :
            fx, fy = fire.pop()
            for dx, dy in directions :
                x, y = dx + fx, dy + fy
                if 0 <= x < R and 0 <= y < C and maze[x][y] != "#" and maze[x][y] != "F" :
                    maze[x][y] = "F"
                    new_fire.append((x,y))
        return new_fire

    def BFS(jh) :
        new_jh = []
        while jh:
            jx, jy = jh.pop()
            if maze[jx][jy] == "F" :
                continue
            for dx, dy in directions :
                x, y = dx + jx, dy + jy
                if x < 0 or x >= R or y < 0 or y >= C :
                    return new_jh, True
                if 0 <= x < R and 0 <= y < C and maze[x][y] == "." :
                    maze[x][y] = "V"
                    new_jh.append((x,y))
        return new_jh, False

    count = 0
    while True :
        count += 1
        jh, flag = BFS(jh)
        if flag :
            print(count)
            break
        if not jh :
            print("IMPOSSIBLE")
            break
        fire = flame(fire)





if __name__ == "__main__" :
    input = sys.stdin.readline
    R, C = map(int, input().split())
    maze = []    
    jh = []
    fire = []
    for x in range(R) :
        maze.append(list(str(input().strip())))
        for y in range(C) :
            if maze[x][y] == "J" :
                jh.append((x,y))
                maze[x][y] == "V"
            elif maze[x][y] == "F" :
                fire.append((x,y))

    solution(R, C, maze, jh, fire)


# 2nd trial -> 틀렸습니다
# flame if문에 maze[x][y] != "F" 추가로 중복 방문 횟수 줄여주면서 메모리 초과 해결
# import sys
# from collections import deque

# def solution(R, C, maze, jh, fire) :
#     directions = [(0,1),(0,-1),(1,0),(-1,0)]

#     def flame(fire) :
#         new_fire = []
#         while fire :
#             fx, fy = fire.pop()
#             for dx, dy in directions :
#                 x, y = dx + fx, dy + fy
#                 if 0 <= x < R and 0 <= y < C and maze[x][y] != "#" and maze[x][y] != "F" :
#                     maze[x][y] = "F"
#                     new_fire.append((x,y))
#         return new_fire

#     def BFS(jh) :
#         new_jh = []
#         while jh:
#             jx, jy = jh.pop()
#             for dx, dy in directions :
#                 x, y = dx + jx, dy + jy
#                 if x < 0 or x >= R or y < 0 or y >= C :
#                     return new_jh, True
#                 if 0 <= x < R and 0 <= y < C and maze[x][y] == "." :
#                     maze[x][y] = "V"
#                     new_jh.append((x,y))
#         return new_jh, False

#     count = 0
#     while True :
#         count += 1
#         jh, flag = BFS(jh)
#         if flag :
#             print(count)
#             break
#         if not jh :
#             print("IMPOSSIBLE")
#             break
#         fire = flame(fire)





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     R, C = map(int, input().split())
#     maze = []    
#     jh = []
#     fire = []
#     for x in range(R) :
#         maze.append(list(str(input().strip())))
#         for y in range(C) :
#             if maze[x][y] == "J" :
#                 jh.append((x,y))
#                 maze[x][y] == "V"
#             elif maze[x][y] == "F" :
#                 fire.append((x,y))

#     solution(R, C, maze, jh, fire)





# first trial - 메모리 초과..ㅋㅋㅋ.ㅋㅋ
# import sys
# from collections import deque

# def solution(R, C, maze, jh, fire) :
#     directions = [(0,1),(0,-1),(1,0),(-1,0)]

#     def flame(fire) :
#         new_fire = []
#         while fire :
#             fx, fy = fire.pop()
#             for dx, dy in directions :
#                 x, y = dx + fx, dy + fy
#                 if 0 <= x < R and 0 <= y < C and maze[x][y] != "#" :
#                     maze[x][y] = "F"
#                     new_fire.append((x,y))
#         return new_fire

#     def BFS(jh) :
#         new_jh = []
#         while jh:
#             jx, jy = jh.pop()
#             for dx, dy in directions :
#                 x, y = dx + jx, dy + jy
#                 if x < 0 or x >= R or y < 0 or y >= C :
#                     return new_jh, True
#                 if 0 <= x < R and 0 <= y < C and maze[x][y] == "." :
#                     maze[x][y] = "V"
#                     new_jh.append((x,y))
#         return new_jh, False

#     count = 0
#     while True :
#         count += 1
#         jh, flag = BFS(jh)
#         if flag :
#             print(count)
#             break
#         if not jh :
#             print("IMPOSSIBLE")
#             break
#         fire = flame(fire)





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     R, C = map(int, input().split())
#     maze = []    
#     jh = []
#     fire = []
#     for x in range(R) :
#         maze.append(list(str(input().strip())))
#         for y in range(C) :
#             if maze[x][y] == "J" :
#                 jh.append((x,y))
#                 maze[x][y] == "V"
#             elif maze[x][y] == "F" :
#                 fire.append((x,y))

#     solution(R, C, maze, jh, fire)



