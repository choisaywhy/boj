import sys

def solution(N, D, shortcusts):
    shortcusts.sort()
    dp = [i for i in range(D+1)]
    dp[0] = 0

    for roads in shortcusts:
        s,d,l = roads
        if d > D: # 고속도로 벗어남
            continue

        dp[d] = min(min(dp[s], s) + l, dp[d])
        for i in range(d+1,D+1):
            if dp[i] < dp[d] + i - d:
                break
            dp[i] = dp[d] + i - d

        # dp[D] = min(dp[D], dp[d] + D - d)

    print(dp[D])





if __name__ == "__main__" :
    input = sys.stdin.readline
    N, D = map(int, input().split())
    shortcusts = [list(map(int, input().split())) for _ in range(N)]
    solution(N, D, shortcusts)