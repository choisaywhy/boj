import sys

def steps(N):
    dp=[[0 for _ in range(10)] for _ in range(N+1)]
    dp[1] = [0] + [1] * 9

    for i in range(2,N+1):
        for j in range(10):
            if not j :
                dp[i][j] = dp[i-1][j+1]
            elif not j-9 :
                dp[i][j] = dp[i-1][j-1]
            else : 
                dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]

    return sum(dp[N])


N = int(sys.stdin.readline())
print(steps(N)% 1000000000)

