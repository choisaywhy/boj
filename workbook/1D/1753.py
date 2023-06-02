import sys
import heapq as hq

def solution(V,E,K,graph):

    routes = [1e9] * (V+1)
    routes[K] = 0

    queue = [(routes[K],K)]

    while queue:
        dist, node = hq.heappop(queue)
        if routes[node] < dist: # 하나의 노드에 여러 간선이 존재하기 때문에
            continue
        for v,w in graph[node]:
            if routes[v] <= dist + w:
                continue
            routes[v] = dist + w
            hq.heappush(queue, (routes[v], v))
    
      
    for i in range(1,V+1):
        ans = "INF"
        if routes[i] != 1e9:
            ans = routes[i]
        print(ans)

                


if __name__ == "__main__" :
    input = sys.stdin.readline
    V, E = map(int,input().split())
    K = int(input())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
    solution(V,E,K,graph)




# import sys
# from collections import deque

# def solution(V,E,K,graph):

#     for i in range(1,E+1):
#         if not graph[i]:
#             continue
#         graph[i].sort(key = lambda x: x[1])
    

#     def find(u):
#         if parents[u] != u:
#             parents[u] = find(parents[u])
#         return parents[u]

#     def union(u,v):
#         pu, pv = find(u), find(v)
#         parents[pu] = pv # directed


#     for i in range(1,V+1):
#         parents = [i for i in range(V+1)]

#         if K == i:
#             print(0)
#             continue

#         stack = deque([(K,0)])
#         ans = "INF"

#         while stack:
#             node, routes = stack.popleft()
#             if node == i:
#                 ans = routes
#                 break

#             for v,w in graph[node]:
#                 if find(node) == find(v): # 이미 확인한 노드
#                     continue
#                 stack.append((v,routes+w))
#                 union(node, v)
        
#         print(ans)
