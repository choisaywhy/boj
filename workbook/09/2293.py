import sys

def solution(n,k,coins):
    dp = [0 for _ in range(k+1)]
    dp[0] = 1

    for coin in coins :
        for i in range(coin,k+1) :
            dp[i] += dp[i-coin]

    print(dp[-1])



if __name__ == "__main__" :
    input = sys.stdin.readline
    n,k = map(int, input().split())
    coins = [ int(input()) for _ in range(n)]
    solution(n,k,coins)