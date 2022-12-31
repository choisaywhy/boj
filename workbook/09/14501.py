import sys

def solution(N, consult):
    dp = [0]*(N+1)

    for day in range(N-1, -1, -1) :
        if consult[day][0] + day <= N :
            dp[day] = max(consult[day][1] + dp[day + consult[day][0]], dp[day + 1])
        else :
            dp[day] = dp[day+1]


    print(dp[0])



if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    consult = [list(map(int, input().split())) for _ in range(N)]
    solution(N, consult)