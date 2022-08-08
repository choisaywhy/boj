import sys

def solution(N,A):
    dp = [0 for _ in range(N+1)]

    if N >= 1:
        dp[1] = A[1]
    if N >= 2:
        dp[2] = A[1] + A[2]
    if N >= 3:    
        dp[3] = max(A[1]+A[3], A[2]+A[3])

    if N >= 4 :
        for i in range(4, N+1):
            dp[i] = max(dp[i-2]+A[i], dp[i-3]+A[i-1]+A[i])
    return dp[N]

N = int(sys.stdin.readline())
A = [0] + list(int(sys.stdin.readline()) for _ in range(N))
print(solution(N,A))