# https://www.acmicpc.net/workbook/view/7309

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
buildings = [int(input()) for _ in range(N)]
stack = deque()
answer = 0

for i in range(N-1,-1,-1) :
    while stack and buildings[stack[-1]] < buildings[i]:
        stack.pop()
    if stack :
        answer += stack[-1] - (i+1)
    else :
        answer += N - (i+1)
    stack.append(i)

print(answer)
