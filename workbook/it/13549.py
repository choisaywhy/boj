import sys
from collections import deque

def solution(N, K):
    
    def BFS(loc):
        queue = deque([loc]) # (현재 위치, 시간)
        visited = [100001]*(100001)
        visited[loc] = 0
        
        while queue:
            cur = queue.popleft()
            if cur == K:
                return visited[K]
            for next in [cur*2, cur+1, cur-1]:
                if 0 <= next < 100001:
                    if next == cur*2 and visited[next] > visited[cur]:
                        queue.append(next)
                        visited[next] = visited[cur]
                    elif visited[next] > visited[cur]+1:
                        queue.append(next)
                        visited[next] = visited[cur]+1
                    
    if K <= N:
        print(N-K)
    else:
        print(BFS(N))


if __name__ == "__main__" :
    input = sys.stdin.readline
    N, K = map(int, input().split())
    solution(N, K)



# import sys
# import heapq

# def solution(N, K):
    
#     def BFS(loc):
#         queue = ([(loc,0)]) # (현재 위치, 시간)
#         visited = [False]*(100001)
#         visited[loc] = True
        
#         while queue:
#             cur, time = queue.popleft()
#             if cur == K:
#                 return time
#             for next in [cur*2, cur+1, cur-1]:
#                 if 0 <= next < 100001 and not visited[next]:
#                     if next == cur*2:
#                         queue.append((next, time))
#                     else:
#                         queue.append((next, time+1))
#                     visited[next] = True
                    
#     if K <= N:
#         print(N-K)
#     else:
#         print(BFS(N))


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, K = map(int, input().split())
#     solution(N, K)