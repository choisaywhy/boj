import sys

def solution(N,L,R,A):
    
    def DFS(node):
        stack = [node]
        total = A[node[0]][node[1]]
        visited[node[0]][node[1]] = True
        union = [node]
        
        while stack:
            x, y = stack.pop()
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx, ny = dx + x, dy + y
                if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
                    continue
                if not (L <= abs(A[x][y] - A[nx][ny]) <= R):
                    continue
                
                visited[nx][ny] = True
                stack.append((nx,ny))
                total += A[nx][ny]
                union.append((nx,ny))
        
        if len(union) == 1:
            visited[node[0]][node[1]] = False
            return False

        total //= len(union)
        for r, c in union:
            A[r][c] = total
        return True
    
    
    day = 0

    while True:
        flag = False
        visited = [[False]*N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if visited[r][c]:
                    continue
                if DFS((r,c)):
                    flag = True
        if not flag:
            break

        day += 1
        
        

    print(day)



if __name__ == "__main__" :
    input = sys.stdin.readline
    N,L,R = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    solution(N,L,R,A)



# import sys

# def solution(N,L,R,A):
    
#     def DFS(node):
#         stack = [node]
#         visited = [[False]*N for _ in range(N)]
#         total = A[node[0]][node[1]]
#         country = 1
        
#         while stack:
#             x, y = stack.pop()
#             for dx, dy in [(0,1),(1,0)]:
#                 nx, ny = dx + x, dy + y
#                 if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
#                     continue
#                 if not (L <= abs(A[x][y] - A[nx][ny]) <= R):
#                     continue
                
#                 visited[nx][ny] = True
#                 stack.append((nx,ny))
#                 total += A[nx][ny]
#                 country += 1
        
#         if country == 1:
#             return False

#         total //= country
#         for r in range(N):
#             for c in range(N):
#                 if not visited[r][c]:
#                     continue
#                 A[r][c] = total
#         return True
    
#     count = 0
#     day = 0

#     while count < N*N-1:
#         print('ddd')
#         for r in range(N):
#             for c in range(N):
#                 if r == N-1 and c == N-1:
#                     continue
#                 if not DFS((r,c)):
#                     count += 1

#         day += 1
#         count = 0
        
        

#     print(day)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N,L,R = map(int, input().split())
#     A = [list(map(int, input().split())) for _ in range(N)]
#     solution(N,L,R,A)