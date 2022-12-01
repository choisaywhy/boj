import sys

def steps(N):
    dp = [[0 for _ in range(10)] for _ in range(N+1)]
    dp[1] = [1] * 10

    for x in range(2,N+1):
        for y in range(10):
            dp[x][y] = dp[x][y-1] + dp[x-1][y]

    return sum(dp[N])


N = int(sys.stdin.readline())
print(steps(N)% 10007)
