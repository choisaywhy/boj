# slicing 을 이용한 연산 (시간 초과)
import sys
from collections import deque

string = deque()
for s in str(sys.stdin.readline()).strip():
    string.append(s)

cursor = deque()
N = int(sys.stdin.readline())


for _ in range(N):
    operation = list(map(str,sys.stdin.readline().split()))

    if operation[0] == 'P' :
        string.append(operation[1])
    elif operation[0] == 'L' :
        if not string :
            continue
        cursor.append(string.pop())

    elif operation[0] == 'D':
        if not cursor :
            continue
        string.append(cursor.pop())

    elif operation[0] == 'B':
        if not string :
            continue
        string.pop()


for a in string + deque(reversed(cursor)):
    print(a, end='')