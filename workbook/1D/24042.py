import sys
from heapq import *

def solution(n,m,crosswalk):
    queue = [(0,1)]
    routes = [1e11]*(n+1)
    routes[1] = 0
    ans = 0
    

    while queue:
        curr_time, node = heappop(queue)
        
        if routes[node] < curr_time:
            continue

        for next, next_time in crosswalk[node]:
            cost = curr_time + (next_time - curr_time) % m

            if routes[next] <= cost + 1:
                continue
            routes[next] = cost + 1
            heappush(queue, (cost + 1, next))

    print(routes[n])



if __name__ == "__main__" :
    input = sys.stdin.readline
    n,m = map(int,input().split())
    crosswalk = [[] for _ in range(n+1)]
    for i in range(m):
        u,v = map(int,input().split())
        crosswalk[u].append((v,i))
        crosswalk[v].append((u,i))
    solution(n,m,crosswalk)





# 1st trial
# import sys
# from heapq import *

# def solution(n,m,crosswalk):
#     queue = [(0,1)]
#     routes = [1e9]*(n+1)
#     routes[1] = 0
#     ans = 0

    

#     while queue:
#         currtime, node, dist = heappop(queue)
        
#         if routes[node] < dist:
#             continue

#         for next, time in crosswalk[node]:
#             if routes[next] <= time + dist:
#                 continue










# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n,m = map(int,input().split())
#     crosswalk = [[] for _ in range(n+1)]
#     for i in range(1,m+1):
#         u,v = map(int,input().split())
#         crosswalk[u].append((v,i))
#         crosswalk[v].append((u,i))
#     solution(n,m,crosswalk)