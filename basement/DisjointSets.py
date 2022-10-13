# 서로소 집합 알고리즘
# 무방향 그래프 사이클 유무 탐색
# reference // https://techblog-history-younghunjo1.tistory.com/257

import sys
input = sys.stdin.readline

# find 연산
def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산
def union_parent(parent, x, y) :
    X = find_parent(parent, x)
    Y = find_parent(parent, y)

    parent[max(X,Y)] = min(X,Y)
    return parent

V, E = int(input()) # vertex length
parent = [num for num in range(V+1)]

for _ in range(E) :
    x, y = map(int, input().split())
    if find_parent(parent, x) == find_parent(parent, y) :
        print('사이클 존재')
        break
    parent = union_parent(parent, x,y)