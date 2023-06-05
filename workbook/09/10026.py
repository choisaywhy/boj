
# 84 ms
import sys
from collections import deque

def solution(n,drawing):

    def bfs(x,y,blindflag):
        queue = deque([(x,y)])

        if blindflag and drawing[x][y] == "G":
            drawing[x][y] = "R"

        while queue:
            nx, ny = queue.popleft()
            
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                if not ( 0 <= dx + nx < n and 0 <= dy + ny < n ) or visited[dx+nx][dy+ny] :
                    continue
                if blindflag and drawing[dx+nx][dy+ny] == "G":
                    drawing[dx+nx][dy+ny] = "R"

                if drawing[dx+nx][dy+ny] != drawing[nx][ny]:
                    continue

                queue.append((dx+nx, dy+ny))
                visited[dx+nx][dy+ny] = True

    
    visited = [[False]*n for _ in range(n)]
    nonblind = 0

    for x in range(n):
        for y in range(n):
            if visited[x][y]:
                continue
            bfs(x,y,False)
            nonblind += 1

    visited = [[False]*n for _ in range(n)]
    blind = 0
    for x in range(n):
        for y in range(n):
            if visited[x][y]:
                continue
            bfs(x,y,True)
            blind += 1
    
    print(nonblind, blind)

    




if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    drawing = [ list(input().strip()) for _ in range(n) ]
    solution(n,drawing)


# 1st trial success 80ms
# import sys
# from collections import deque

# def solution(n,drawing):

#     def bfs(x,y,blindflag):
#         queue = deque([(x,y)])

#         while queue:
#             nx, ny = queue.popleft()
            
#             for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
#                 if not ( 0 <= dx + nx < n and 0 <= dy + ny < n ) or visited[dx+nx][dy+ny] :
#                     continue
#                 if not blindflag and drawing[dx+nx][dy+ny] != drawing[nx][ny]:
#                     continue
#                 if blindflag and [drawing[dx+nx][dy+ny], drawing[nx][ny]].count("B") == 1:
#                     continue
#                 queue.append((dx+nx, dy+ny))
#                 visited[dx+nx][dy+ny] = True

    
#     visited = [[False]*n for _ in range(n)]
#     nonblind = 0

#     for x in range(n):
#         for y in range(n):
#             if visited[x][y]:
#                 continue
#             bfs(x,y,False)
#             nonblind += 1

#     visited = [[False]*n for _ in range(n)]
#     blind = 0
#     for x in range(n):
#         for y in range(n):
#             if visited[x][y]:
#                 continue
#             bfs(x,y,True)
#             blind += 1
    
#     print(nonblind, blind)

    

    





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     drawing = [ list(input().strip()) for _ in range(n) ]
#     solution(n,drawing)