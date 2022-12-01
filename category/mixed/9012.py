import sys
from collections import deque

def solution(operation) :
    stack = deque()

    for op in operation :
        if op == '(' :
            stack.append(1)
        elif op == ')' :
            if not stack :
                return 'NO'
            else :
                stack.pop()
        
    if not stack :
        return 'YES'
    else :
        return 'NO'



N = int(sys.stdin.readline())

for _ in range(N):
    operation = str(sys.stdin.readline())
    print(solution(operation))