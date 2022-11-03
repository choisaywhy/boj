import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
array = deque()
answer = []
count = 0

for target in [int(input()) for _ in range(n)] :
    for num in range(count+1, n+1) :
        if not array or num <= target:
            array.append(num)
            answer.append('+')
            count = num
    if array[-1] == target :
        array.pop()
        answer.append('-')


if not array :
    for a in answer:
        print(a)
else :
    print("NO")
