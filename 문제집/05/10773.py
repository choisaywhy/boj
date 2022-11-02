# https://www.acmicpc.net/workbook/view/7309

import sys
from collections import deque

input = sys.stdin.readline

K = int(input())
answer = deque()
for _ in range(K) :
    num = int(input())
    if answer and num == 0 :
        answer.pop()
        continue
    answer.append(num)

print(sum(answer))