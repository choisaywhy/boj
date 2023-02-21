import sys
from collections import deque

def solution(N, K, D):
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    dp = [0] * (N+1)

    for _ in range(K) :
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    
    W = int(input())
    
    queue = deque()
    for i in range(1, N+1) :
        if indegree[i] == 0 :
            queue.append(i)
            dp[i] = D[i]
    
    while queue :
        node = queue.popleft()
        for next in graph[node] :
            indegree[next] -= 1
            dp[next] = max(dp[node]+D[next], dp[next])
            if indegree[next] == 0:
                queue.append(next)
    
    print(dp[W])
    print('dp',dp)

if __name__ == "__main__" :
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T) :
        N, K = map(int, input().split())
        D = [0] + list(map(int, input().split()))
        solution(N, K, D)







# import sys
# from collections import deque

# def solution(N, K, D):
#     graph = [[] for _ in range(N+1)]
#     inDegree = [0 for _ in range(N+1)]
#     depth = []
#     queue = deque()

#     for _ in range(K) :
#         x, y = map(int, input().split())
#         graph[x].append(y)
#         inDegree[y] += 1
    
#     W = int(input())
#     print('graph',graph, 'indegree',inDegree)
#     if inDegree[W] == 0 :
#         print('early end',D[W])
#         return
    
#     for i in range(1, N+1) :
#         if inDegree[i] == 0 :
#             queue.append(i)
#     print('starting queue',queue)
#     while queue :
#         node = queue.pop()
#         print('node',node)
#         if node == W :
#             print('node reached end')
#             break
#         depth.append(graph[node])
#         print('depth updated',depth)
#         for next in graph[node] :
#             inDegree[next] -= 1
        
#             if inDegree[next] == 0 :
#                 queue.append(next)
#     print('and the answer is',depth)




# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     T = int(input())
#     for _ in range(T) :
#         N, K = map(int, input().split())
#         D = [0] + list(map(int, input().split()))
#         solution(N, K, D)







# reversed graph 사용하여 처리 하려 했으나,
# depth 고려 없이 중복되는 노드 발생
# import sys
# from collections import deque

# def solution(N, K, D):
#     graph = [[] for _ in range(N+1)] # reversed graph
#     redepth = [[] for _ in range(N+1)]
#     visited = [False]*(N+1)
#     for _ in range(K) :
#         x, y = map(int, input().split())
#         graph[y].append(x)
#     print('graph',graph)
#     W = int(input())

#     if graph[W] == [] :
#         print('early end',D[W])
#     else :
#         queue = deque([(W,0)])
#         redepth[0].append(D[W])
#         print('queue',queue)
#         print('redepth',redepth)
#         while queue :
#             node, depth = queue.popleft()
#             print('node',node,'depth',depth,'turn')
#             for next in graph[node] :
#                 print('next',next,'turn')
#                 redepth[depth+1].append(D[next])
#                 visited[next] = True
#                 queue.append((next, depth+1))
#                 print('queue updated',queue)
#                 print('redepth updated', redepth)
        
#         print('and the answer',redepth)


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     T = int(input())
#     for _ in range(T) :
#         N, K = map(int, input().split())
#         D = [0] + list(map(int, input().split()))
#         solution(N, K, D)



# 목표 건물 직전 depth 중복 처리 문제 발생
# depth 별 저장 공간 생성해보기
# import sys
# from collections import deque

# def solution(N, K, D):
#     graph = [[] for _ in range(N+1)]
#     inDegree = [0 for _ in range(N+1)]
#     ans = 0
#     queue = deque()

#     for _ in range(K) :
#         x, y = map(int, input().split())
#         graph[x].append(y)
#         inDegree[y] += 1
    
#     end = int(input())

#     print('graph',graph)
#     print('indegree',inDegree)
    
#     if inDegree[end] == 0 :
#         print(D[end])
#         return
    
#     for i in range(1, N) :
#         if inDegree[i] == 0 :
#             queue.append(i)
#             ans += D[i]
    
#     print('queue',queue)

#     while queue :
#         buliding = queue.popleft()
#         print(buliding,'turn')
#         maxTime = 0
#         for next in graph[buliding] :
#             if next == end :
#                 print('reached end')
#                 ans += D[next]
#                 print('final ans',ans, D[next])
#                 print('ans is',ans)
#                 return

#             if D[next] > maxTime :
#                 print(next,D[next],'is bigger than', maxTime)
#                 maxTime = D[next]
#                 print(maxTime,'amxtime updated')
#             inDegree[next] -= 1

#             if inDegree[next] == 0 :
#                 print(next,'degree reached 0')
#                 if next not in queue :
#                     queue.append(next)
#                 print(queue,'queue updated')
#         ans += maxTime
#         print(ans,'ans updated')



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     T = int(input())
#     for _ in range(T) :
#         N, K = map(int, input().split())
#         D = [0] + list(map(int, input().split()))
#         solution(N, K, D)