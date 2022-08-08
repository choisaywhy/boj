import sys

def solution(N,A):
    dp = A[:]

    for i in range(N):
        for j in range(i):
            if A[i] > A[j] :
                dp[i] = max(dp[j] + A[i], dp[i])
    return max(dp)

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
print(solution(N,A))

