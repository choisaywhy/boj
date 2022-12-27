import sys

def solution(N, M, arr, K):
    dp = [[0]*(M+1) for _ in range(N+1)]
    for n in range(1,N+1) :
        for m in range(1,M+1) :
            dp[n][m] = dp[n-1][m] + dp[n][m-1] + arr[n-1][m-1] - dp[n-1][m-1]

    for _ in range(K) :
        i, j, x, y = map(int, input().split())
        print(dp[x][y]- dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])



if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    K = int(input())
    solution(N, M, arr, K)


# 시간 초과 without dp
#  import sys

# def solution(N, M, arr, K):
#     for _ in range(K) :
#         i, j, x, y = map(int, input().split())
#         ans = 0

#         for n in range(i-1, x) :
#             for m in range(j-1, y) :
#                 ans += arr[n][m]

#         print(ans)


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M = map(int,input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     K = int(input())
#     solution(N, M, arr, K)






# 문제 해석 오류
# import sys

# def solution(N, M, arr, K):
#     dp = [0 ]* (M * N + 1)

#     for n in range(N) :
#         for m in range(M) :
#             dp[n*M+m+1] = dp[n*M+m] + arr[n][m]

#     print(dp)
#     for _ in range(K) :
#         i,j,x,y = map(int, input().split())

#         if j == y :
#             ans = sum([arr[][i] for i in range(j,y+1)])
#             print()
#         else :
#             print(dp[(x-1)*M+(y-1)+1]-dp[(i-1)*M+(j-1)])



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M = map(int,input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     K = int(input())
#     solution(N, M, arr, K)



