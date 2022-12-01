import sys

def solution(N,A):
    dp = A[:]

    for i in range(1,N):
        dp[i] = max(dp[i], dp[i-1]+A[i])

    return max(dp)

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
print(solution(N,A))