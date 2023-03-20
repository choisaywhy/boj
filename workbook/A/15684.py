import sys

def solution(N, M, H, ladder):
    if M == 0:
        print(0)
        return 
        
    def play_ladder():
        for i in range(1,N+1):
            cur = i
            for j in range(1,H+1):
                cur += ladder[j][cur]
            if cur != i:
                return False
        return True

    def DFS(depth, index):
        nonlocal ans

        if depth >= ans:
            return
        
        if play_ladder():
            ans = min(ans, depth)
            return
        
        for i in range(index, len(bridges)):
            x, y = bridges[i]
            if ladder[x][y] != 0:
                continue

            if y+1 <= N and ladder[x][y+1] != 1:
                ladder[x][y], ladder[x][y+1] = 1, -1
                DFS(depth+1, i+1)
                ladder[x][y], ladder[x][y+1] = 0, 0
    ans = 4
    bridges = []
    for j in range(1,N+1):
        for i in range(1,H+1):
            if ladder[i][j] != 0:
                continue
            if j+1 <= N and ladder[i][j+1] != 1:
                bridges.append((i,j))
    DFS(0, 0)
    if ans > 3:
        print(-1)
    else:
        print(ans)





if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M, H = map(int, input().split())
    ladder = [[0]*(N+1) for _ in range(H+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        ladder[a][b] = 1 # 오른쪽으로 이어진 사다리
        ladder[a][b+1] = -1 # 왼쪽으로 이어진 사다리

    
    solution(N, M, H, ladder)


# import sys

# def solution(N, M, H, ladder):
#     ans = 4

#     def play_ladder():
#         count = 0
#         for i in range(1,N+1):
#             cur = i
#             for j in range(1,H+1):
#                 if ladder[j][cur] == 1:
#                     cur += 1
#                 elif ladder[j][cur] == -1:
#                     cur -= 1

#             if cur == i:
#                 count += 1
        
#         if count == N:
#             return True
#         return False

#     def DFS(depth):
#         nonlocal ans

#         if depth >= ans:
#             return
        
#         if play_ladder():
#             ans = min(ans, depth)
#             return
        
#         for j in range(1,N+1):
#             for i in range(1,H+1):
#                 if ladder[i][j] != 0:
#                     continue

#                 if j+1 <= N and ladder[i][j+1] != 1:
#                     ladder[i][j], ladder[i][j+1] = 1, -1
#                     DFS(depth+1)
#                     ladder[i][j], ladder[i][j+1] = 0, 0
#     if M == 0:
#         print(0)
#     else:
#         DFS(0)
#         if ans > 3:
#             print(-1)
#         else:
#             print(ans)





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M, H = map(int, input().split())
#     ladder = [[0]*(N+1) for _ in range(H+1)]
#     for _ in range(M):
#         a, b = map(int, input().split())
#         ladder[a][b] = 1 # 오른쪽으로 이어진 사다리
#         ladder[a][b+1] = -1 # 왼쪽으로 이어진 사다리

    
#     solution(N, M, H, ladder)