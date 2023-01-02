import sys

def solution(N,M,maze):
    
    dp = [[0]*(M+1) for _ in range(N+1)]

    for x in range(1,N+1) :
        for y in range(1,M+1) :
            dp[x][y] = max(dp[x-1][y-1], dp[x-1][y], dp[x][y-1]) + maze[x-1][y-1]
    print(dp[-1][-1])


if __name__ == "__main__" :
    input = sys.stdin.readline
    N,M = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(N)]
    solution(N,M,maze)