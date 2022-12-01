import sys

N = int(sys.stdin.readline())
deque = []

for _ in range(N):
    operation = list(map(str,sys.stdin.readline().split()))

    if operation[0] == 'push_front' :
        deque = [int(operation[1])] + deque
    if operation[0] == 'pop_front' :
        if not deque :
            print(-1)
            continue
        print(deque.pop(0))
    if operation[0] == 'push_back' :
        deque += [int(operation[1])]
    if operation[0] == 'pop_back' :
        if not deque :
            print(-1)
            continue
        print(deque.pop())
    if operation[0] == 'size' :
        print(len(deque))
    if operation[0] == 'empty' :
        if not deque :
            print(1)
            continue
        print(0)
    if operation[0] == 'front' :
        if not deque :
            print(-1)
            continue
        print(deque[0])
    if operation[0] == 'back' :
        if not deque :
            print(-1)
            continue
        print(deque[-1])


