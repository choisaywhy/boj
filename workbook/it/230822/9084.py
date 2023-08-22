import sys
def solution():
    n = int(input())
    coins = list(map(int,input().split()))
    m = int(input())

    dp = [[0]*(m+1) for _ in range(n)]
    
    for i in range(n):
        for j in range(1,m+1):
            if i == 0 and j % coins[i] == 0:
                dp[i][j] = 1
                continue
            if j < coins[i]:
                dp[i][j] = dp[i-1][j]
            elif j == coins[i]:
                dp[i][j] = dp[i-1][j] + 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]

    print(dp[-1][-1])
    
    


if __name__ == "__main__" :
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        solution()
