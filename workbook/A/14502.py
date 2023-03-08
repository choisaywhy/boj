# https://www.acmicpc.net/source/57080913 참고하여 시간 줄여 볼 것
import sys
from collections import deque

def solution(N, M, lab, virus, wall):
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    ans = 0
    def virusBFS():
        queue = deque(virus)
        
        visited = virus[:]

        while queue:
            node = queue.popleft()
            x,y = node

            if N*M-len(visited)-wall-3 <= ans: # 남은 안전 지대 수가 ans를 넘어버리면
                break
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < N and 0 <= ny < M) or (nx,ny) in visited:
                    continue
                if lab[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited.append((nx,ny))
        return len(visited)
    
    def wallDFS(depth):
        nonlocal ans
        if depth == 3:
            ans = max(ans, N*M-virusBFS()-wall-3)
            return
        
        for x in range(N):
            for y in range(M):
                if lab[x][y] != 0:
                    continue
                lab[x][y] = 1
                wallDFS(depth+1)
                lab[x][y] = 0


    wallDFS(0)
    print(ans)


if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    lab = []
    virus = []
    wall = 0
    for x in range(N):
        lab.append(list(map(int ,input().split())))
        for y in range(M):
            if lab[x][y] == 2:
                virus.append((x,y))
            elif lab[x][y] == 1:
                wall += 1


    solution(N, M, lab, virus, wall)







# 1st trial
# import sys
# from collections import deque

# def solution(N, M, lab, virus, wall, void):
#     directions = [(1,0),(0,1),(-1,0),(0,-1)]
#     ans = 0
#     def virusBFS():
#         queue = deque(virus)
#         visited = virus[:]

#         while queue:
#             node = queue.popleft()
#             x,y = node

#             if N*M-len(visited)-wall-3 <= ans: # 남은 안전 지대 수가 ans를 넘어버리면
#                 break
            
#             for dx, dy in directions:
#                 nx, ny = x + dx, y + dy
#                 if not (0 <= nx < N and 0 <= ny < M) or (nx,ny) in visited:
#                     continue
#                 if lab[nx][ny] == 0:
#                     queue.append((nx,ny))
#                     visited.append((nx,ny))
#         return len(visited)
    
#     def wallDFS(depth):
#         nonlocal ans
#         if depth == 3:
#             ans = max(ans, N*M-virusBFS()-wall-3)
#             return
        
#         for nx,ny in void:
#             if lab[nx][ny] != 0:
#                 continue
#             lab[nx][ny] = -1
#             wallDFS(depth+1)
#             lab[nx][ny] = 0

    
#     for x,y in void:
#         lab[x][y] = 1
#         wallDFS(1)
#         lab[x][y] = 0

#     print(ans)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M = map(int, input().split())
#     lab = []
#     virus = []
#     void = []
#     wall = 0
#     for x in range(N):
#         lab.append(list(map(int ,input().split())))
#         for y in range(M):
#             if lab[x][y] == 2:
#                 virus.append((x,y))
#             elif lab[x][y] == 1:
#                 wall += 1
#             else:
#                 void.append((x,y))

#     solution(N, M, lab, virus, wall, void)


