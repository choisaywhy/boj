import sys
def solution():
    n = int(input())
    
    nums = list(map(int,input().split()))
    dp = nums[:]
    
    for i in range(1,n):
        dp[i] = max(dp[i-1]+nums[i], nums[i])

    print(max(dp))

if __name__ == "__main__" :
    input = sys.stdin.readline

    solution()
