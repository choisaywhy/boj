import sys
from collections import defaultdict

def solution():
    n,m = map(int,input().split())
    lamp = defaultdict(int)
    for _ in range(n):
        lamp[tuple(map(int, input().strip()))] += 1
    k = int(input())
    ans = 0

    for key,val in sorted(lamp.items(), key= lambda x : x[1], reverse=True):
        zero = key.count(0)

        if k >= zero and (k - zero) % 2 == 0:
            ans = val
            break

    print(ans)


if __name__ == "__main__" :
    input = sys.stdin.readline

    solution()
