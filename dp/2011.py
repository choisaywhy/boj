import sys

def solution(N):
    nums = {1:(0,1,2,3,4,5,6,7,8,9), 2:(0,1,2,3,4,5,6)}
    dp = [0 for _ in range(len(N)+1)]

    if not int(N[0]) :
        return 0
    dp[0], dp[1] = 1, 1

    for i in range(2, len(N)+1) :
        if int(N[i-2]) in nums.keys() :
            if int(N[i-1]) in nums[int(N[i-2])]:
                dp[i] += dp[i-2]
        elif not int(N[i-1]) :
            return 0

        if int(N[i-1]):
            dp[i] += dp[i-1]

    return dp[-1] % 1000000


N = str(sys.stdin.readline()).rstrip()
print(solution(N))