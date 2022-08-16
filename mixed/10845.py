import sys
from collections import deque

N = int(sys.stdin.readline())
queue = []

for _ in range(N):
    operation = list(map(str,sys.stdin.readline().split()))

    if operation[0] == 'push' :
        queue += [int(operation[1])]
    if operation[0] == 'pop' :
        if not queue :
            print(-1)
            continue
        print(queue.pop(0))
    if operation[0] == 'size' :
        print(len(queue))
    if operation[0] == 'empty' :
        if not queue :
            print(1)
            continue
        print(0)
    if operation[0] == 'front' :
        if not queue :
            print(-1)
            continue
        print(queue[0])
    if operation[0] == 'back' :
        if not queue :
            print(-1)
            continue
        print(queue[-1])


