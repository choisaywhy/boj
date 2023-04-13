import sys

def solution(a, b):
    dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    
    for x in range(1,len(a)+1):
        for y in range(1,len(b)+1):
            if a[x-1] == b[y-1]:
                dp[x][y] = dp[x-1][y-1]+1
                continue
            dp[x][y] = max(dp[x][y-1] ,dp[x-1][y])
    print(dp[-1][-1])






if __name__ == "__main__" :
    input = sys.stdin.readline
    a = list(map(str, input().strip()))
    b = list(map(str, input().strip()))
    solution(a, b)