import sys
from math import sqrt

input = sys.stdin.readline
Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int,input().split())
speed = sqrt((Bx-Ax)**2 + (By-Ay)**2) / sqrt((Dx-Cx)**2 + (Dy-Cy)**2)


for g in guess :
    mid = 0
    start = 0
    end = len(card) - 1
    flag = False

    while start <= end :
        mid = (start + end) // 2
        if card[mid] < g :
            start = mid + 1
        elif card[mid] > g :
            end = mid - 1
        else :
            flag = True
            break
    if flag :
        print(counting[g],end=" ")
    else :
        print(0,end=" ")
        
