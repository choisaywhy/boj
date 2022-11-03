# https://www.acmicpc.net/workbook/view/7309

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
stack = deque()
res = []

for i in range(N-1,-1,-1) :
    while stack and stack[-1] <= arr[i] :
        stack.pop()
    if stack :
        res.append(stack[-1])
    else :
        res.append(-1)
    stack.append(arr[i])

print(" ".join(list(map(str, reversed(res))))) 