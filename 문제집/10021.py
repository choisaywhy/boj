import sys
import heapq as hq

input = sys.stdin.readline

def find_parent(parent, v) :
    if parent[v] != v :
        parent[v] = find_parent(parent, parent[v])
    return parent[v]

def union_parent(parent, v1, v2) :
    v1 = find_parent(parent, v1)
    v2 = find_parent(parent, v2)

    parent[max(v1, v2)] = min(v1, v2)
    return parent

def distance(v1, v2) :
    x1, y1 = v1
    x2, y2 = v2
    return (x1 - x2)** 2 + (y1- y2)**2

N, C = map(int, input().split())
field = [tuple(map(int, input().split())) for _ in range(N)] # x, y
edge = []
parent = [i for i in range(N)]
cost = 0
count = 0


for i in range(N-1) :
    for j in range(i+1, N) :
        dist = distance(field[i], field[j])
        if dist >= C :
            hq.heappush(edge, (dist, i, j))


flag = False
for _ in range(len(edge)) :
    dist, i, j = hq.heappop(edge)
    if find_parent(parent, i) == find_parent(parent, j):
        continue
    parent = union_parent(parent, i, j)
    cost += dist
    count += 1

    if count == N-1 :
        flag = True
        break

if flag :
    print(cost)
else :
    print(-1)