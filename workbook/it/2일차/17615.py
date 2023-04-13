import sys

def solution(n, balls):
    prev = -1

    for i in range(n-2,-1,-1):
        if balls[prev] == balls[i]:
            continue
        prev = 0





if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    balls = list(map(str, input().strip()))
    solution(n, balls)