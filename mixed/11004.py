import sys


def solution(K,nums):
    nums.sort()
    return nums[K-1]

N, K = list(map(int,sys.stdin.readline().split()))
nums = list(map(int,sys.stdin.readline().split()))

print(solution(K,nums))