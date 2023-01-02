import sys
sys.setrecursionlimit(10 ** 6)

def solution(M,N,maps):
    dp = [[-1]*(N) for _ in range(M)]
    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    def DFS(x,y) :
        if x == M - 1 and y == N - 1:
            return 1
        
        if dp[x][y] == -1 :
            dp[x][y] = 0

            for d in directions :
                nx, ny = x + d[0], y + d[1]
                
                if 0 <= nx < M and 0 <= ny < N and maps[x][y] > maps[nx][ny] :
                    dp[x][y] += DFS(nx,ny)
        return dp[x][y]
    
    print(DFS(0,0))




if __name__ == "__main__" :
    input = sys.stdin.readline
    M, N = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(M)]
    solution(M,N,maps)

# import sys

# def solution(M,N,maps):
#     dp = [[0]*(N) for _ in range(M)]
#     directions = [(0,1),(0,-1),(1,0),(-1,0)]
#     dp[0][0] = 1

#     for x in range(M) :
#         for y in range(N):
#             print(x,y,'turn')
#             for d in directions :

#                 px, py = x + d[0], y + d[1]
#                 if 0 <= px < M and 0 <= py < N and maps[x][y] < maps[px][py] :
#                     dp[x][y] += dp[px][py]
#             print('final dp',x,y,dp[x][y])
#             print('updated',dp)
#     print(dp)





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     M, N = map(int, input().split())
#     maps = [list(map(int, input().split())) for _ in range(M)]
#     solution(M,N,maps)