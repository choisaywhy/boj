import sys

# def solution(n):





if __name__ == "__main__" :
    input = sys.stdin.readline
    t = int(input())
    q = [int(input()) for _ in range(t)]
    target = max(q)
    dp = [0]*(target+1)

    if target >= 1:
        dp[1] = 1
    if target >= 2:
        dp[2] = 2
    if target >= 3:
        dp[3] = 4
    if target >= 4:
        for i in range(4,target+1):
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009

    for a in q:
        print(dp[a])