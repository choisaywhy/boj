import sys

def solution(N,M,board,max_num):
    ans = 0
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    def DFS(depth, count, node, visited):
        nonlocal ans
        x, y = node

        if count + max_num * (4 - depth) <= ans:
            return

        if depth == 4: # 모든 블럭 iter 완
            ans = max(ans, count)
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M) or (nx,ny) in visited:
                continue

            visited.append((nx,ny))
            if depth == 2: # 3번째 블럭 끝나고 depth 2
                DFS(depth+1, count+board[nx][ny], (x,y), visited)
            else:
                DFS(depth+1, count+board[nx][ny], (nx,ny), visited)
            visited.pop()


    for x in range(N):
        for y in range(M):
            DFS(1,board[x][y],(x,y),[(x,y)])

    print(ans)


if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_num = max(map(max, board))
    
    solution(N,M,board,max_num)




# 1st trail -> success
# import sys

# def solution(N,M,board):
#     tetromiro = [[(0,0),(0,1),(0,2),(0,3)],
#         [(0,0),(1,0),(2,0),(3,0)],
#         [(0,0),(1,0),(0,1),(1,1)],
#         [(0,0),(1,0),(2,0),(2,1)],
#         [(0,1),(1,1),(2,1),(2,0)],
#         [(0,0),(0,1),(1,1),(2,1)],
#         [(0,0),(0,1),(1,0),(2,0)],
#         [(0,0),(1,0),(1,1),(1,2)],
#         [(0,2),(1,1),(1,2),(1,0)],
#         [(0,0),(0,1),(0,2),(1,2)],
#         [(0,0),(1,0),(0,1),(0,2)],
#         [(0,0),(1,0),(1,1),(2,1)],
#         [(0,1),(1,1),(1,0),(2,0)],
#         [(1,0),(1,1),(0,1),(0,2)],
#         [(0,0),(0,1),(1,1),(1,2)],
#         [(0,1),(1,0),(1,1),(1,2)],
#         [(0,0),(0,1),(0,2),(1,1)],
#         [(0,0),(1,0),(1,1),(2,0)],
#         [(0,1),(1,1),(1,0),(2,1)]]
    
#     ans = 0
#     for x in range(N):
#         for y in range(M):
#             count = 0
#             for tet in tetromiro: # 19 경우의 수
#                 count = 0
#                 for t in tet:
#                     tx, ty = t
#                     if not (0 <= x+tx < N and 0 <= y+ty < M):
#                         count = 0
#                         break
#                     count += board[x+tx][y+ty]
#                 ans = max(count, ans)
    
#     print(ans)




# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M = map(int, input().split())
#     board = []
#     for _ in range(N):
#         board.append(list(map(int, input().split())))

#     solution(N,M,board)

