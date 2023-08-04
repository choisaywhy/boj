import sys

def solution():
    n,m = map(int,input().split())
    dp = [[0]*m for _ in range(n)]
    
    for x in range(n):
        for y in range(m):
            if x == 0 or y == 0: # 상,좌 쪽의 좌표는 경로 1로 지정
                dp[x][y] = 1
                continue
            dp[x][y] = (dp[x-1][y]+dp[x][y-1]+dp[x-1][y-1]) % (10**9+7) 

    
    print(dp[-1][-1])

if __name__ == "__main__" :
    input = sys.stdin.readline
    
    solution()
