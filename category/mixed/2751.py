import sys

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums += [int(sys.stdin.readline())]

for num in sorted(nums):
    print(num)