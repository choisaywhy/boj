import sys

def solution(N,A):
    dp_left = [1 for _ in range(N)]
    dp_right = [1 for _ in range(N)]


    for k in range(N):
        for i in range(k):
            if A[i] < A[k]:
                dp_left[k] = max(dp_left[k], dp_left[i] + 1)

    for k in range(N-1,-1,-1):
        for j in range(N-1,k,-1):
            if A[k] > A[j] :
                dp_right[k] = max(dp_right[k], dp_right[j] + 1) 

    dp = [left+right for left, right in zip(dp_left, dp_right)]

    return max(dp) -1 

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
print(solution(N,A))