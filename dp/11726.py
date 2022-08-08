import sys
from math import factorial as fac


N = int(input())
dp=[0 for _ in range(N+1)]
dp[0],dp[1] = 1,1

for target in range(2, N+1):
    dp[target] = dp[target-1]+dp[target-2]

print(dp[N] % 10007)









# 일반식 도출로 풀이 시도
# N = int(input())
# answer = 0

# for i in range(N//2 + 1): # 1 * 2 모양의 사각형 수
#     j = N - (i * 2)       # 2 * 1 모양의 사각형 수
#     print('i, j : ',i,j)
#     if not i or not j :
#         answer += 1
#         print(answer)
#         continue
#     if i >= j :
#         answer += fac(i+1)/(fac(j)*fac(i+1-j))
#     elif i < j :
#         answer += fac(j+1)/(fac(i)*fac(j+1-i))
#     print(answer)


# print(answer % 10007)