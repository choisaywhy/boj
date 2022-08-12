import sys
from math import sqrt

def solution(N, K):
    dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

    
    for k in range(K+1):
        dp[k][0] = 1

    for k in range(1,K+1):
        for n in range(1,N+1):
            dp[k][n] = sum([dp[i][n-1] for i in range(1, k+1)])
    
    return dp[K][N] % 1000000000


N, K = list(map(int, sys.stdin.readline().split()))
print(solution(N, K ))