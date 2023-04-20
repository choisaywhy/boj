import sys

def solution(N, K, stuffs):
    
    dp = [[0]*(K+1) for _ in range(N+1)]

    for x in range(1,N+1):
        w,v = stuffs[x-1]
        for y in range(1,K+1):
            if y < w:
                dp[x][y] = dp[x-1][y]
            dp[x][y] = max(dp[x-1][y], dp[x][w]+ dp[x-1][y-w])
    print(dp[-1][-1])





if __name__ == "__main__" :
    input = sys.stdin.readline
    N, K = map(int, input().split())
    stuffs = [tuple(map(int, input().split())) for _ in range(N)]
    solution(N, K, stuffs)