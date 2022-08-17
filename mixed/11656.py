import sys

nums = str(sys.stdin.readline()).strip()
suffix = []

for _ in range(len(nums)):
    suffix.append(nums)
    nums = nums[1:]

for s in sorted(suffix):
    print(s)