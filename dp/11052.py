import sys

def solution(N,P):
    dp = [0 for _ in range(N+1)]


    for i in range(1,N+1):
        temp = [P[i]]
        for j in range(1,i//2+1):
            temp += [dp[i-j]+dp[j]]
        dp[i] = max(temp)

    return dp[-1]


N = int(sys.stdin.readline())
P = [0] + list(map(int, sys.stdin.readline().split()))
print(solution(N,P))