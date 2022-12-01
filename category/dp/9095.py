import sys

length = int(sys.stdin.readline())

for _ in range(length):
    N = int(sys.stdin.readline())
    if N == 1:
        print(1)
        continue
    elif N == 2:
        print(2)
        continue

    dp=[0]*(N+1)
    dp[0],dp[1], dp[2] = 1,1,2

    for target in range(3, N+1):
        dp[target] = dp[target-1]+dp[target-2]+dp[target-3]

    print(dp[N])