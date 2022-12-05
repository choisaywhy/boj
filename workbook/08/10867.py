import sys

def solution(N, arr):
    for a in sorted(set(arr)) :
        print(a, end=" ")




if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    solution(N, arr)