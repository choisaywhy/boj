import sys

def solution(a,b):
    print(int(str(int(a[::-1])+int(b[::-1]))[::-1]))



if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        a, b = map(str, input().strip().split())
        solution(a,b)