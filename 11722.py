import sys

def solution(N,A):
    dp = [1 for _ in range(N)]

    for i in range(N) :
        for j in range(i) :
            if A[i] < A[j] :
                dp[i] = max(dp[j]+1, dp[i])

    return max(dp)

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
print(solution(N,A))

