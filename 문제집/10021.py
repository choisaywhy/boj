import sys
from collections import deque

input = sys.stdin.readline

def DFS() :
    stack = deque([])
    visited = [False * N]

N, C = map(int, input().split())
fields = [tuple(map(int, input().split())) for _ in range(N)]

print(fields)
if N == 1 :
    pass


