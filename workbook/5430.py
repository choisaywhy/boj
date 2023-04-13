import sys
from collections import deque
def solution(p,n,x):

    x = deque(x)
    rev = False

    for func in p:
        if func == 'R':
            rev = not rev
        elif func == 'D':
            if not x:
                print("error")
                return
            if rev:
                x.pop()
                continue
            x.popleft()

    if rev:
        x.reverse()
    print('[',",".join(x),']', sep="")






if __name__ == "__main__" :
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        p = input().strip()
        n = int(input())
        x = input().strip()[1:-1].split(",")
        if not n:
            x = []
        solution(p,n,x)