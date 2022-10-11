import sys

input = sys.stdin.readline

N, K = map(int, input().split())
cargo = [[0,0]] # 직접 조회하지 않아도 됨으로 사실상 필요없는 선언
dp = [[0]*(K+1) for _ in range(N+1)]
for _ in range(N) :
    cargo.append(list(map(int, input().split())))

for n in range(1, N+1) :
    for k in range(1, K+1) :
        if k < cargo[n][0] :
            dp[n][k] = dp[n-1][k]
        else :
            # print('n : ',n,'k : ',k, dp[n-1][k],'비교', cargo[n][1] ,'+', dp[n-1][K-cargo[n][0]],'(',K-cargo[n][0],')')
            dp[n][k] = max(dp[n-1][k], cargo[n][1] + dp[n-1][k-cargo[n][0]])


print(dp[-1][-1])


# 간결화 된 코드
# import sys

# input = sys.stdin.readline

# N, K = map(int, input().split())
# bag = [[0]* (K+1) for _ in range(N+1)] 

# for i in range(1,N+1):
#     W, V = map(int, input().split())

#     for j in range(1,K+1) :
#         if W > j :
#             bag[i][j] = bag[i-1][j]
#         else :
#             bag[i][j] = max(bag[i-1][j], bag[i-1][j-W]+V)
# print(bag)