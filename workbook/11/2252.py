# 시간 개선
# graph dict형태 생성 후 get 요청하는 것 보다, list index 접근이 더 효율적임
# 2540ms -> 180ms
import sys
from collections import deque

def solution(N, M):
    graph = [[] for _ in range(N+1)]
    queue = deque()
    linked = [0] * (N+1)
    ans = []

    for _ in range(M) :
        a, b = map(int, input().split())
        graph[a].append(b)
        linked[b] += 1
    
    for i in range(1, N+1) :
        if linked[i] == 0 :
            queue.append(i)

    while queue :
        node = queue.popleft()
        ans.append(node)
        for next in graph[node] :
            linked[next] -= 1

            if linked[next] == 0 :
                queue.append(next)
    
    print(*ans)


if __name__ == "__main__" :
    input = sys.stdin.readline
    
    N, M = map(int, input().split())

    solution(N, M)



# 통과
# import sys
# from collections import deque

# def solution(N, M):
#     graph = {}
#     queue = deque()
#     linked = [0] * (N+1)
#     ans = []

#     for _ in range(M) :
#         a, b = map(int, input().split())
#         graph[a] = graph.get(a, []) + [b]
#         linked[b] += 1
    
#     for i in range(1, N+1) :
#         if linked[i] == 0 :
#             queue.append(i)

#     while queue :
#         node = queue.popleft()
#         ans.append(node)
#         for next in graph.get(node, []) :
#             linked[next] -= 1

#             if linked[next] == 0 :
#                 queue.append(next)
    
#     print(*ans)


# if __name__ == "__main__" :
#     input = sys.stdin.readline
    
#     N, M = map(int, input().split())

#     solution(N, M)

    

# debugging ver
# import sys
# from collections import deque

# def solution(N, M):
#     graph = {}
#     queue = deque()
#     linked = [0] * (N+1)
#     ans = []

#     for _ in range(M) :
#         a, b = map(int, input().split())
#         graph[a] = graph.get(a, []) + [b]
#         linked[b] += 1
    
#     for i in range(1, N+1) :
#         if linked[i] == 0 :
#             queue.append(i)
#     print('about to start with', queue)

#     while queue :
#         print('new queue',queue)
#         node = queue.popleft()
#         ans.append(node)
#         print('node turn',node,'ans updated',ans)
#         for next in graph.get(node, []) :
#             linked[next] -= 1

#             if linked[next] == 0 :
#                 queue.appendleft(next)
    
#     print(ans, graph, linked)





# if __name__ == "__main__" :
#     input = sys.stdin.readline
    
#     N, M = map(int, input().split())

#     solution(N, M)