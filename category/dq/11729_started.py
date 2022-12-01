import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

circles = {1:deque([i for i in range(1,N+1)]), 2:deque(), 3:deque()}

def hanoi(circles) :
    target = circles[1].pop()

    if not circles[2] :
        pass

