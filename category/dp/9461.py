import sys
from math import sqrt

def solution(N):
    dp = [0,1,1,1,2,2,3,4,5] + [0 for _ in range(N-8)]

    for i in range(9, N+1):
        dp[i] = dp[i-1] + dp[i-5]
    
    return dp[N]


T = int(sys.stdin.readline())
for test in range(T):
    N = int(sys.stdin.readline())
    print(solution(N))