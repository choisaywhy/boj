import sys

def steps(N):
    dp = [[0 for _ in range(2)] for _ in range(N+1)]
    dp[1] = [0,1]

    for x in range(2,N+1):
        for y in range(2):
            if not y :
                dp[x][y] = dp[x-1][y] + dp[x-1][y+1]
            else :
                dp[x][y] = dp[x-1][y-1]

    return sum(dp[N])


N = int(sys.stdin.readline())
print(steps(N))
