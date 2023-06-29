import sys

def solution(n):
    print(int((n*4-3)**.5))





if __name__ == "__main__" :
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        x, y = map(int,input().split())
        n = y - x
        solution(n)

    