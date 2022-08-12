import sys
from math import sqrt

def solution(N):
    
    if N % 2 :
        return 0

    dp = [0 for _ in range(N+1)]

    if N >= 2:
        dp[2] = 3

    for i in range(4, N+1):
        if i % 2:
            dp[i] = 0
            continue
        dp[i] = dp[i-2]*3 + sum(dp[:i-3]) * 2 + 2
    return dp[-1]

N = int(sys.stdin.readline())
print(solution(N))