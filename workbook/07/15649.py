import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

for c in list(combinations([str(i) for i in range(1,N+1)], M)) :
    print(" ".join(c))