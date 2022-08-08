import sys
from math import sqrt

def solution(N):
    
    dp = [0 for _ in range(N+1)]

    sqrtnum = []

    for i in range(1,N+1):
        temp = []
        if sqrt(i) == int(sqrt(i)):
            dp[i] = 1
            sqrtnum += [i]
            continue
        for num in sqrtnum:
            temp += [dp[num] + dp[i-num]]
        
        dp[i] = min(temp)
    
    return dp[N]

N = int(sys.stdin.readline())
print(solution(N))







# 가장 가까운 제곱수를 이용한 풀이
# 반례 41
# import sys
# from math import sqrt

# def solution(N):
    
#     dp = [0 for _ in range(N+1)]

#     sqrtnum = 0

#     for i in range(1,N+1):
#         if sqrt(i) == int(sqrt(i)):
#             dp[i] = 1
#             sqrtnum = i
#             continue

#         dp[i] = dp[sqrtnum] + dp[i-sqrtnum]
#     print(dp)
#     return dp[N]

# N = int(sys.stdin.readline())
# print(solution(N))