import sys

def solution(N, arr):
    for a in sorted(set(arr)) :
        print(a)




if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    solution(N, arr)