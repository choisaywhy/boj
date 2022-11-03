import sys
from collections import deque

input = sys.stdin.readline

def BFS(start, k, graph) :
    sv, sr = start
    queue = deque([start])
    visited = [False] * (N+1)
    visited[sv] = True
    count = 0

    while queue :
        v, r = queue.popleft()
        for nv, nr in graph[v] :
            if visited[nv] :
                continue
            visited[nv] = True
            queue.append((nv, min(r, nr)))
            if min(r, nr) >= k :
                count += 1
    return count


graph = {}
N, Q = map(int, input().split())

for _ in range(N-1) :
    p, q, r = map(int, input().split())
    graph[p] = graph.get(p, []) + [(q,r)]
    graph[q] = graph.get(q, []) + [(p,r)]

for _ in range(Q) :
    k, v = map(int, input().split())
    print(BFS((v,1000000001), k, graph))