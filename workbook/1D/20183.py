import sys
from heapq import *

def solution(n,m,a,b,c,roads,fees):

    def dijkstra(limit):
        queue = [(0,a)] # 현재 노드까지의 총 금액, 현재 노드
        routes = [[1e15,0] for _ in range(n+1)] # 현재 노드까지의 최소 금액 , 현재 노드까지 경로 내의 최대 요금
        routes[a] = [0,0]

        while queue:
            cost, node = heappop(queue)
            if routes[node][0] < cost:
                continue

            for next, next_cost in roads[node]:
                if routes[next][0] <= cost + next_cost:
                    continue
                if next_cost > limit or c < cost + next_cost: # 정한 fee보다 크거나, 가진 돈을 초과하거나
                    continue
                routes[next] = [cost + next_cost, max(next_cost, routes[node][1])]

                heappush(queue, (routes[next][0], next))

        return routes[b][1]


    fees = sorted(list(set(fees)))
    flag = False
    start = 0
    end = len(fees) 

    while start < end:
        mid = (start + end) // 2

        target = dijkstra(fees[mid])
        
        if target == 0: # limitation이 너무 작아 갈 수 있는 경로가 충분하지 않구나
            start = mid + 1
        else:
            flag = True
            end = mid
    
    print(fees[start] if flag else -1)


if __name__ == "__main__" :
    input = sys.stdin.readline
    n,m,a,b,c = map(int,input().split())
    roads = [[] for _ in range(n+1)]
    fees = []
    for _ in range(m):
        u,v,w = map(int,input().split())
        roads[u].append((v,w))
        roads[v].append((u,w))
        fees.append(w)

    
    solution(n,m,a,b,c,roads,fees)



# 2nd trial with binary search debugging ver
# import sys
# from heapq import *

# def solution(n,m,a,b,c,roads,fees):

#     def dijkstra(limit):
#         queue = [(0,a)] # 현재 노드까지의 총 금액, 현재 노드
#         routes = [[1e15,0] for _ in range(n+1)] # 현재 노드까지의 최소 금액 , 현재 노드까지 경로 내의 최대 요금
#         routes[a] = [0,0]

#         while queue:
#             cost, node = heappop(queue)
#             if routes[node][0] < cost:
#                 continue

#             for next, next_cost in roads[node]:
#                 if routes[next][0] <= cost + next_cost:
#                     continue
#                 if next_cost > limit or c < cost + next_cost: # 정한 fee보다 크거나, 가진 돈을 초과하거나
#                     continue
#                 routes[next] = [cost + next_cost, max(next_cost, routes[node][1])]

#                 heappush(queue, (routes[next][0], next))

#         return routes[b][1]


#     fees = sorted(list(set(fees)))
#     flag = False
#     start = 0
#     end = len(fees) 

#     while start < end:
#         mid = (start + end) // 2
#         print('limitation gonna be',fees[mid])
#         print('start',start,'end',end,'mid',mid)

#         target = dijkstra(fees[mid])
#         print('dijkstras result is', target)
        
#         if target == 0: # limitation이 너무 작아 갈 수 있는 경로가 충분하지 않구나
#             start = mid + 1
#         else:
#             flag = True
#             end = mid
    
#     print(fees[start] if flag else -1)


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n,m,a,b,c = map(int,input().split())
#     roads = [[] for _ in range(n+1)]
#     fees = []
#     for _ in range(m):
#         u,v,w = map(int,input().split())
#         roads[u].append((v,w))
#         roads[v].append((u,w))
#         fees.append(w)

    
#     solution(n,m,a,b,c,roads,fees)


# debugging ver
# 1st trial 시간초과 nmlogn
# import sys
# from heapq import *

# def solution(n,m,a,b,c,roads,fees):

#     def dijkstra(limit):
#         queue = [(0,a)] # 현재 노드까지의 총 금액, 현재 노드
#         routes = [[1e15,0] for _ in range(n+1)] # 현재 노드까지의 최소 금액 , 현재 노드까지 경로 내의 최대 요금
#         routes[a] = [0,0]

#         while queue:
#             cost, node = heappop(queue)
#             print(cost, node, routes, routes[node])
#             if routes[node][0] < cost:
#                 continue

#             for next, next_cost in roads[node]:
#                 if routes[next][0] <= cost + next_cost:
#                     continue
#                 if next_cost > limit or c < cost + next_cost: # 정한 fee보다 크거나, 가진 돈을 초과하거나
#                     continue
#                 routes[next] = [cost + next_cost, max(next_cost, routes[node][1])]

#                 heappush(queue, (routes[next][0], next))
        
#         print('and the outcome is',routes)
#         print(routes[b])

#         if routes[b][0] == 1e15:
#             return False
#         return routes[b][1]


#     fees = sorted(list(set(fees)))
#     ans = -1

#     for fee in fees:
#         print('if ',fee,' is the largest')
#         dij = dijkstra(fee)
#         if dij:
#             ans = dij
#             break
    
#     print(ans)






# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n,m,a,b,c = map(int,input().split())
#     roads = [[] for _ in range(n+1)]
#     fees = []
#     for _ in range(m):
#         u,v,w = map(int,input().split())
#         roads[u].append((v,w))
#         roads[v].append((u,w))
#         fees.append(w)

    
#     solution(n,m,a,b,c,roads,fees)