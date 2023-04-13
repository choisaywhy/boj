import sys

def solution(n, coins, total):
    target = total//2
    dp = [False]*(target+ 1)
    dp[0] = True

    for types, num in coins.items():
        for i in range(target, types-1, -1):
            if not dp[i-types]:
                continue
            for j in range(num):
                if i + types*j > target:
                    break
                dp[i + types*j] = True

            if dp[-1]:
                break

    print(1 if dp[-1] else 0)




if __name__ == "__main__" :
    input = sys.stdin.readline
    for _ in range(3):
        n = int(input())
        coins = {}
        total = 0
        for _ in range(n):
            types, num = map(int, input().split())
            total += types*num
            coins[types] = num
        if total%2:
            print(0)
            continue
        
        solution(n, coins,total)