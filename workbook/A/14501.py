import sys

def solution(N, consulting):
    dp = [0] * (N+1)

    for day in range(N-1, -1, -1):
        t, c = consulting[day]

        if day + t <= N:
            dp[day] = max(c + dp[day + t], dp[day + 1])
        else :
            dp[day] = dp[day+1]


    print(dp[0])

if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    consulting = [tuple(map(int, input().split())) for _ in range(N)]

    solution(N, consulting)
