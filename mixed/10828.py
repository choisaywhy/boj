import sys
from collections import deque

N = int(sys.stdin.readline())
stack = deque()

for _ in range(N):
    operation = list(map(str,sys.stdin.readline().split()))

    if operation[0] == 'push' :
        stack.append(int(operation[1]))
    if operation[0] == 'pop' :
        if not stack :
            print(-1)
        else :
            print(stack.pop())
    if operation[0] == 'size' :
        print(len(stack))
    if operation[0] == 'empty' :
        if not stack :
            print(1)
        else :
            print(0)
    if operation[0] == 'top' :
        if not stack :
            print(-1)
        else :
            print(stack[-1])

