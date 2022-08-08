import sys

N = int(sys.stdin.readline())
dp = [0]*(N+1)

for target in range(2,N+1):
    dp[target] = dp[target - 1] + 1
    if not target % 3:
        dp[target] = min(dp[target], dp[target // 3] + 1)
    if not target % 2:
        dp[target] = min(dp[target], dp[target // 2] + 1)

print(dp[N])





# by BFS 시간초과,,ㅋㅋㅋ
# def bfs(start):
#     queue = deque()
#     visited = deque()
#     answer = 0

#     queue.append(start)

#     while queue:
#         num, dist = queue.popleft()
#         if [num, dist] not in visited:
#             visited.append([num, dist])
#             if not num % 3:
#                 if num / 3 == 1 :
#                     answer = dist + 1
#                     break   
#                 queue.append([num / 3, dist + 1])
#             if not num % 2:
#                 if num / 2 == 1 :
#                     answer = dist + 1
#                     break  
#                 queue.append([num / 2, dist + 1])
#             if num - 1 == 1 :
#                     answer = dist + 1
#                     break  
#             queue.append([num-1, dist + 1])
#     return answer


# N = int(sys.stdin.readline())
# print(bfs([N, 0]))
