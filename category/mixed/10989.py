import sys

N = int(sys.stdin.readline())
nums = [0] * 10001


for _ in range(N):
    num = int(sys.stdin.readline())
    nums[num] += 1

for i in range(1,len(nums)):
    if not nums[i] :
        continue
    for _ in range(nums[i]):
        print(i)
