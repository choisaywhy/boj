from os import link
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
tree = {}

for _ in range(N-1):
    x, y = list(map(int, input().split()))
    tree[x] = tree.get(x,[])+[y]
    tree[y] = tree.get(y,[])+[x]


def traversal(node,target,visited = []) :
    print('target',target,'node',node)
    visited.append(node)
    for next in tree[node] :
        if target == next :
            print(node)
        if next not in visited:
            traversal(next,target,visited)


for _ in range(2,N+1):
    traversal(1,_)
