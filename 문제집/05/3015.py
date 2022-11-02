import sys 
from collections import deque

input = sys.stdin.readline
N = int(input())
heights = [int(input()) for _ in range(N)]
stack = deque()
res = 0

for i in range(N-1,-1,-1) :
    flag = False
    print('i',i,'heights',heights[i])
    while stack and heights[stack[-1]] < heights[i] :
        stack.pop()
        res += 1
        flag = True
    if stack:
        res += 1
    print(res,'res')

    stack.append(i)
    print(stack,'stack')
print(res)