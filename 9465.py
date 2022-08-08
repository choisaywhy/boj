import sys

def solution(N, dp):
    for y in range(1,N) : # 1,2, , ,N-1
        for x in range(2) : # 0,1
            if not x :
                if y == 1:
                    dp[x][y] += dp[x+1][y-1]
                else :
                    dp[x][y] += max(dp[x+1][y-2],dp[x+1][y-1])
            else : # if x == 1
                if y == 1:
                    dp[x][y] += dp[x-1][y-1]
                else :
                    dp[x][y] += max(dp[x-1][y-2],dp[x-1][y-1])
    return max(max(dp[0]), max(dp[1]))


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    dp = []
    dp.append(list(map(int, sys.stdin.readline().split())))
    dp.append(list(map(int, sys.stdin.readline().split())))
    print(solution(N,dp))
