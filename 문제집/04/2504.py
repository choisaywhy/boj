import sys
from collections import deque

input = sys.stdin.readline
bracket = str(input().strip())
queue = deque()
answer = 0
count = 0
flag = False
for b in bracket :
    if b == '[' or '(' :
        if flag :
            answer += count
        queue.append('b')
        flag = False
    elif b == ']' :
        count += 3
        flag = True
    elif b == ')' :
        count += 2
        flag = True
print(answer)