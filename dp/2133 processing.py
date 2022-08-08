import sys
from math import sqrt

def solution(N):
    
    if N % 2 :
        return 0

    dp = [0 for _ in range(N//2+1)]

    if N // 2 >= 2:
        dp[2] = 3

    for i in range(N//2+1):
        dp[i] = 3 ** (N//2)

    
    return dp[-1]

N = int(sys.stdin.readline())
print(solution(N))