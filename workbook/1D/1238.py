# 2nd trial 
# 경로 뒤집어서 dijkstra 연산 n -> 2번으로 줄이기
import sys
from heapq import *

def solution(n,m,x,routes,routesrev):
    

    def dijkstra(start,route):

        time = [1e8]*(n+1)
        time[start] = 0
        queue = [(0,start)]

        while queue:
            t, u = heappop(queue)

            if time[u] < t:
                continue

            for v,w in route[u]:
                if time[v] <= t + w:
                    continue
                time[v] = t + w
                heappush(queue, (time[v], v))

        return time
    
    going = dijkstra(x, routesrev) # 1~n -> x 마을 까지 거리 
    returning = dijkstra(x, routes) # x -> 1~n 마을 까지 거리
    ans = 0

    for i in range(1,n+1):
        if ans < going[i] + returning[i]:
            ans = going[i] + returning[i]
            
    print(ans)



if __name__ == "__main__" :
    input = sys.stdin.readline
    
    n,m,x = map(int, input().split())
    routes = [[] for _ in range(n+1)]
    routesrev = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int, input().split())
        routes[u].append((v,w))
        routesrev[v].append((u,w))

    solution(n,m,x,routes,routesrev)


# 1st trial -> 성공 928ms
# import sys
# from heapq import *

# def solution(n,m,x,routes):
    

#     def dijkstra(start):

#         time = [1e8]*(n+1)
#         time[start] = 0
#         queue = [(0,start)]

#         while queue:
#             t, u = heappop(queue)

#             if time[u] < t:
#                 continue

#             for v,w in routes[u]:
#                 if time[v] <= t + w:
#                     continue
#                 time[v] = t + w
#                 heappush(queue, (time[v], v))

#         return time
    
#     going = dijkstra(x) # 1~n -> x 마을 까지 거리 
#     ans = 0

#     for i in range(1,n+1):
#         if i == x:
#             continue
#         returning = dijkstra(i)[x] # x -> 1~n 마을 까지 거리

#         if ans >= going[i] + returning:
#             continue
#         ans = going[i] + returning

    
#     print(ans)
    




# if __name__ == "__main__" :
#     input = sys.stdin.readline
    
#     n,m,x = map(int, input().split())
#     routes = [[] for _ in range(n+1)]
#     for _ in range(m):
#         u,v,w = map(int, input().split())
#         routes[u].append((v,w))

#     solution(n,m,x,routes)