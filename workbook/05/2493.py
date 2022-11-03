# https://www.acmicpc.net/workbook/view/7289

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
tops = list(map(int,input().split()))
stack = deque()
answer = deque()
for i in range(N) :
    while stack and tops[stack[-1]] < tops[i] :
        stack.pop()
    if stack :
        answer.append(stack[-1] + 1)
    else :
        answer.append(0)
    stack.append(i)

print(" ".join(list(map(str, answer))))
        








# 시간 초과 -> O(N**2)
# answer = []

# for h in range(N) :
#     for i in range(h-1, -1, -1) :
#         if tops[h] <= tops[i] :
#             answer.append(i+1)
#             break
#     if len(answer) != h+1 :
#         answer.append(0)

# print(" ".join(answer), sep="")