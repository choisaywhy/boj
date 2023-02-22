# list sort 진행 후 앞부터 접근이 더 빠름
import sys

def solution(N,M,graph):
    parents = [i for i in range(N+1)]
    cost = 0
    graph.sort()

    def find(a) :
        if parents[a] != a :
            parents[a] = find(parents[a])
        return parents[a]
    
    def union(a, b) :
        pa = find(a)
        pb = find(b)
        parents[max(pa, pb)] = min(pa, pb)

    for i in range(M) :
        c, a, b = graph[i]

        if find(a) == find(b) :
            continue
        union(a,b)
        cost += c

    print(cost)
    

if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    graph = []

    for _ in range(M) :
        a, b, c = map(int, input().split())
        graph.append((c,a,b))
    solution(N,M,graph)


# 정답 with heapq
# import sys
# import heapq

# def solution(N,M,graph):
#     parents = [i for i in range(N+1)]
#     cost = 0
    
#     def find(a) :
#         if parents[a] != a :
#             parents[a] = find(parents[a])
#         return parents[a]
    
#     def union(a, b) :
#         pa = find(a)
#         pb = find(b)
#         parents[max(pa, pb)] = min(pa, pb)

#     for _ in range(M) :
#         c, a, b = heapq.heappop(graph)

#         if find(a) == find(b) :
#             continue
#         union(a,b)
#         cost += c

#     print(cost)
    

# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N = int(input())
#     M = int(input())
#     graph = []

#     for _ in range(M) :
#         a, b, c = map(int, input().split())
#         heapq.heappush(graph, (c,a,b))
#     solution(N,M,graph)