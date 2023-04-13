import sys
from collections import deque
def solution(N,M,route,trip):
    ans = "YES"

    def DFS(root):
        nonlocal ans
        stack = [root]
        visited = [False] * (N+1)
        visited[root] = True
        
        while stack:
            node = stack.pop()
            for next in route[node]:
                if visited[next]:
                    continue
                visited[next] = True
                stack.append(next)
            
        for t in trip:
            if not visited[t]:
                ans = "NO"
                break          

    
    DFS(trip[0])

    print(ans)




if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    route = {}
    for i in range(1,N+1):
        temp = list(map(int, input().split()))
        route[i] = []
        for j in range(N):
            if temp[j] == 1:
                route[i].append((j+1))
    trip = list(map(int, input().split()))
    solution(N,M,route,trip)




# import sys
# from collections import deque
# def solution(N,M,route,trip,routenum):
#     ans = "YES"

#     def DFS(root):
#         nonlocal ans
#         stack = deque([root])
#         target = 0
#         lagged = 0

#         while stack:
#             node = stack.pop()

#             if target == len(trip)-1:
#                 return
#             if lagged > routenum * 3:
#                 ans = "NO"
#                 return

#             if trip[target] in route[node]:
#                 stack.append(trip[target])
#                 target += 1
#                 lagged = 0
#                 continue

#             stack.extend(route[node])
#             lagged += 1



#     DFS(trip[0])
#     print(ans)




# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N = int(input())
#     M = int(input())
#     route = {}
#     routenum = 0
#     for i in range(1,N+1):
#         temp = list(map(int, input().split()))
#         route[i] = []
#         for j in range(N):
#             if temp[j] == 1:
#                 route[i].append((j+1))
#                 routenum += 1
#     trip = list(map(int, input().split()))
#     solution(N,M,route,trip,routenum)