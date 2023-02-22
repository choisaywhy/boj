import sys
import heapq


def solution(V, E):
    parents = [i for i in range(V+1)]
    graph = []
    cost = 0

    def find(node) :
        if parents[node] != node :
            parents[node] = find(parents[node])
        return parents[node] 

    def union(nodex, nodey) :
        parentx = find(nodex)
        parenty = find(nodey)
        parents[max(parentx, parenty)] = min(parentx, parenty)

    
    for _ in range(E) :
        a, b, c = map(int,input().split())
        heapq.heappush(graph, (c,a,b))
    
    for _ in range(E) :
        c, a, b = heapq.heappop(graph)
        if find(a) == find(b) :
            continue
        else :
            union(a, b)
            cost += c

    print(cost)



if __name__ == "__main__" :
    input = sys.stdin.readline
    V, E = map(int, input().split())
    solution(V, E)