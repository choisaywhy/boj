import sys

def solution(N, wine):
    dp = [0] * (N+1)
    
    if N >= 1:
        dp[1] = wine[1]
    if N >= 2:
        dp[2] = dp[1] + wine[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-1],
                    wine[i]+wine[i-1]+dp[i-3],
                    wine[i]+dp[i-2])
    return dp[N]


N = int(sys.stdin.readline())
wine = [0]
for _ in range(N):
    wine.append(int(sys.stdin.readline()))
print(solution(N,wine))