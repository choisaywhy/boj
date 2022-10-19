# https://www.acmicpc.net/workbook/view/7287

# using deque not cursor
import sys
from collections import deque
input = sys.stdin.readline

L = int(input())

for _ in range(L) :
    front = deque()
    back = deque()

    for word in str(input()).strip() :
        if word == "<" :
            if not front : # if front is empty
                continue
            back.appendleft(front.pop())
        elif word == ">" :
            if not back : # if back is empty
                continue
            front.append(back.popleft())
        elif word == "-" :
            if not front : # if front is empty
                continue
            front.pop()
        else :
            front.append(word)
    
    print("".join(front+back))







# using cursor
# 시간초과@!
import sys
from collections import Counter
input = sys.stdin.readline

L = int(input())

for _ in range(L) :
    cursor = 0
    pswd = []
    for word in str(input()).strip() :
        if word == "<" :
            if cursor < 0 :
                continue
            cursor -= 1
        elif word == ">" :
            if cursor > len(pswd)-1 :
                continue
            cursor += 1
        elif word == "-" :
            if cursor == 0 :
                continue
            pswd.pop(cursor)
        else :
            pswd = pswd[:cursor] + [word] + pswd[cursor:]
    
    print("".join(pswd[::-1]))
