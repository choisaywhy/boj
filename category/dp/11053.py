# import sys

# def solution(N, A):
#     dp = [[] for _ in range(N)]
#     dp[0] = [A[0]]
    
#     for a in range(1, N):
#         if A[a] <= dp[a-1][-1]:
#             temp = dp[a-1][:]
#             while temp and A[a] <= max(temp):
#                 temp.pop()
#             temp.append(A[a])
#             dp[a] = max(temp, dp[a-1])

#         else :
#             dp[a] = dp[a-1] + [A[a]]
#         print(dp)
#     return len(dp[N-1])


# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))
# print(solution(N,A))


# import sys

# def solution(N, A):
#     dp = [1 for _ in range(N)]
    
#     for a in range(1, N):
#         if A[a] <= A[a-1]:
#             temp = 0
#             for i in range(2, a+1):
#                 if A[a-i] < A[a] and dp[a-i] > temp:
#                     temp = dp[a-i]
#             dp[a] += max(temp,dp[a-1])
#         else :
#             dp[a] += dp[a-1]
#         print(dp)
#     return dp[N-1]


# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))
# print(solution(N,A))

import sys

def solution(N, A):
    dp = [0 for _ in range(N)]
    
    for i in range(N):
        for j in range(i):
            if A[i] > A[j] and dp[i] < dp[j]:
                dp[i] = dp[j]
        dp[i] += 1
    return max(dp)


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
print(solution(N,A))






# 7
# 5 10 3 30 5 7 20

# 4
