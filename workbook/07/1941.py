import sys
from itertools import combinations
from collections import deque

def solution() :
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    def BFS(check) :
        visited = check[1:]
        queue = deque([check[0]])

        while queue :
            x, y = queue.popleft()
            for dx, dy in directions :
                nx, ny = dx + x, dy + y
                if 0 <= nx < 5 and 0 <= ny < 5 and (nx,ny) in visited :
                    visited.remove((nx,ny))
                    queue.append((nx,ny))

        if visited:
            return False
        return True

    seats = [list(str(input().strip())) for _ in range(5)]

    res = 0
    for arr in combinations(range(25),7) :
        count = sum(map(lambda x : 1 if seats[x//5][x%5] == "S" else 0 , arr))
        if count >= 4 and BFS(list(map(lambda x : (x//5, x%5), arr))) :
            res += 1
    print(res)



if __name__ == "__main__" :
    input = sys.stdin.readline
    solution()





# first trial --> 의도 문제 없으나, 중복 검사 경우 많고 전체를 돌지 못함.
# 과부하 줄일 수 있는 방법, dfs를 가볍헤 할 것
# 다음 턴으로 넘어갈 때 visited = False 로 변환하는 부분에서 막힘

# import sys

# def solution() :
#     directions = [(1,0), (-1,0), (0,1), (0,-1)]
#     def DFS(x, y, countY, depth) :
#         nonlocal count
#         # 백트래킹 부분 또한 손봐야함
#         if countY >= 4 :
#             return 

#         if depth == 7 :
#             count += 1
#             return

#         for dx, dy in directions :
#             nx, ny = dx + x, dy + y
#             if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] :
#                 visited[nx][ny] = True
#                 # print(nx,ny,'visting available')
#                 if seats[nx][ny] == "S" :
#                     DFS(nx, ny, countY, depth+1)
#                 else :
#                     DFS(nx, ny, countY+1, depth+1)
#                 visited[nx][ny] = False


#     seats = []
#     party = []
#     for x in range(5) :
#         seats.append(list(str(input().strip())))

#         for y in range(5) :
#             if seats[x][y] == "S" :
#                 party.append((x,y))
    
#     if len(party) < 4:
#         print(0)
#         return

#     visited = [[False]*5 for _ in range(5)]
#     count = 0
#     for p in party :
#         px, py = p
#         visited[px][py] = True # px, py 를 지나는 모든 행선을 파악했으므로, 더이상 탐색 안함
#         DFS(px, py, 0, 1)
#     print(count)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     solution()