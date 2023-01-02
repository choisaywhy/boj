# # 맞은 코드
# import sys

# def solution(n, k, coins):
#     dp = [10001] * (k+1)
#     dp[0] = 0
#     for coin in coins :
#         for i in range(coin, k+1) :
#             dp[i] = min(dp[i], dp[i-coin] + 1)
#     if dp[-1] == 10001 :
#         print(-1)
#     else :
#         print(dp[-1])

# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n, k = map(int, input().split())
#     coins = []
#     for _ in range(n) :
#         coins.append(int(input()))
#     solution(n, k, coins)

## 틀린 코드
import sys

def solution(n, k, coins):
    coins.sort()
    dp = [10001] * (k+1)
    dp[0] = 0
    for i in range(n) :
        # dp[i] = coins[i]   coin = 1 , index = 0 일때 dp[0]을 1로 만듬
        for j in range(coins[i], k+1) :
            dp[j] = min(dp[j], dp[j - coins[i]]+1)
    if dp[-1] == 10001 :
        print(-1)
    else :
        print(dp[-1])
    



if __name__ == "__main__" :
    input = sys.stdin.readline
    n, k = map(int, input().split())
    coins = []
    for _ in range(n) :
        coins.append(int(input()))
    solution(n, k, coins)