# dont know the answer!

import sys
from collections import deque

def solution(N, spots):
    spots.sort(reversed = True)
    res = [spots.pop()]

    while spots :
        x, y = spots.pop()
        for i in range(len(res)) :
            rx, ry = res[i]
            if x * ry <= rx * y :
                continue
            res.insert(i-1, (x,y))
    print(res)


if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    spots = [tuple(map(int, input().split())) for _ in range(N)]
    solution(N, spots)