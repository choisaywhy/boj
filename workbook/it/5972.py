# debugging ver
import sys
from collections import defaultdict
import heapq 

def solution(N,M,roads):
    dp = [1e9]*(N+1) #### 1001하면 틀림 -> 데이터 수정 요청
    dp[1] = 0

    queue = []
    heapq.heappush(queue, (0, 1))

    while queue:
        cost, node = heapq.heappop(queue)

        for next, ncost in roads[node]:
            if dp[next] <= cost + ncost:
                continue

            dp[next] = cost + ncost
            heapq.heappush(queue, (ncost + cost, next))

    print(dp[N])
        

if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    roads = defaultdict(list)
    for _ in range(M):
        a, b, c = map(int,input().split())
        roads[a].append((b,c))
        roads[b].append((a,c))

    solution(N,M,roads)



# kruskal 시도, but 모든 노드 지나야한다는 조건 없음
# import sys

# def solution(N,M,roads):
#     parents = [i for i in range(N+1)]
#     cows = 0

#     def find(a):
#         if parents[a] != a:
#             parents[a] = find(parents[a])
#         return parents[a]

#     def union(a,b):
#         pa, pb = find(a), find(b)
#         parents[max(pa,pb)] = min(pa,pb)
    
#     for road in roads:
#         a, b, c = road

#         if find(a) == find(b):
#             continue
#         union(a,b)
#         cows += c

#         if parents[N] == 1:
#             break
#     print(parents)
#     print(cows)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M = map(int, input().split())
#     roads = [tuple(map(int, input().split())) for _ in range(M)]
#     roads.sort(key = lambda x:x[2])
    
#     solution(N,M,roads)