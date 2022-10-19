import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    flag = False
    reverse = False
    p = str(input().strip())
    n = int(input())
    if not n :
        array = []
    else :
        array = deque(str(input().strip())[1:-1].split(","))
    for op in p :
        if op == "R" :
            reverse = not reverse
        elif op == "D" :
            if not array :
                flag = True
                break
            if reverse :
                array.pop()
            else :
                array.popleft()

    if flag :
        print("error",end="\n")
    else :
        if reverse :
            array = reversed(array)
        print('[', ",".join(array), ']',sep="",end="\n")