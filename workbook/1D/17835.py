import sys
from heapq import *

def solution(n,m,k,roads_rev,rooms):

    dist = [1e11]*(n+1)
    queue = []

    for room in rooms:
        dist[room] = 0
        heappush(queue, (0, room))


    while queue:
        d, v = heappop(queue)
        if dist[v] < d:
            continue

        for u, c in roads_rev[v]:

            if dist[u] <= d + c:
                continue
            dist[u] = d + c
            heappush(queue, (dist[u], u))


    total_max = max(dist[1:])
    for i in range(1,n+1):
        if dist[i] < total_max:
            continue
        print(i)
        break
    print(total_max)



if __name__ == "__main__" :
    input = sys.stdin.readline
    n,m,k = map(int, input().split())
    roads_rev = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,c = map(int, input().split())
        roads_rev[v].append((u,c))
    
    rooms = list(map(int, input().split()))

    solution(n,m,k,roads_rev,rooms)



# 1st trial
# n*eloge
# import sys
# from heapq import *

# def solution(n,m,k,roads_rev,rooms):


#     total_dist = [1e11]*(n+1)
    
#     for room in range(1,n+1):
#         if not rooms[room]:
#             continue

#         dist = [1e11]*(n+1)
#         dist[room] = 0

#         queue = [(dist[room], room)]

#         while queue:
#             d, v = heappop(queue)
#             if dist[v] < d:
#                 continue

#             for u, c in roads_rev[v]:

#                 if rooms[u] or dist[u] <= d + c:
#                     continue
#                 dist[u] = d + c
#                 heappush(queue, (dist[u], u))
        

#         for i in range(1,n+1):
#             if rooms[i] or total_dist[i] < dist[i]:
#                 continue
#             total_dist[i] = dist[i]
    
#     total_max = [0,0]
#     for i in range(1,n+1):
#         if total_dist[i] < total_max[1] or rooms[i]:
#             continue
#         total_max = [i, total_dist[i]]

    
#     print("\n".join(map(str, total_max)))



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n,m,k = map(int, input().split())
#     roads_rev = [[] for _ in range(n+1)]
#     for _ in range(m):
#         u,v,c = map(int, input().split())
#         roads_rev[v].append((u,c))
    
#     rooms = [False]*(n+1)
#     for room in list(map(int, input().split())):
#         rooms[room] = True
    
#     solution(n,m,k,roads_rev,rooms)