import sys
import heapq as hq
input = sys.stdin.readline

def find(parent, v) :
    if parent[v] != v :
        parent[v] = find(parent, parent[v])
    return parent[v]

def union(parent, A, B): # 이미 A, B가 다른 부모를 가지고 있다는 걸 상정하고 실행
    Ar = find(parent, A)
    Br = find(parent, B)

    parent[max(Ar,Br)] = min(Ar,Br)
    return parent

def kruskal(V, E, edge) :
    parent = [i for i in range(V+1)] # 초기 root 값은 자기 자신으로 초기화
    cost = 0
    for _ in range(E) :
        c, x, y = hq.heappop(edge)
        if find(parent,x) == find(parent, y) : # 부모가 같아 사이클이 존재하는 것으로 판별한 경우
            continue # 최소 신장 트리에 포함하지 않음
        parent = union(parent, x,y)
        cost += c

    return cost
 
 
V, E = map(int, input().split()) # V = vertex 수, E = edge 수
edge = []
for _ in range(E) :
    hq.heappush(edge, tuple(map(int, input().split()))) # cost, A, B 받기

print(kruskal(V, E, edge))



# 크루스칼 알고리즘 구현 코드
# reference // https://techblog-history-younghunjo1.tistory.com/262

# import sys
# import heapq
# input = sys.stdin.readline

# V, E = map(int, input().split())
# parent = [i for i in range(V+1)]
# edge = heapq.heapify([])
# for _ in range(E) :
#     heapq.heappush(edge, tuple(map(int, input().split())))# cost, x, y 받기
# # edge = [tuple(map(int, input().split())) for _ in range(E)] 

# def find(parent, x) :
#     if parent[x] != x :
#         parent[x] = find(parent, parent[x])
#     return parent[x]

# def union(parent, x, y): # 이미 x, y가 다른 부모를 가지고 있다는 걸 상정하고 실행
#     x = find(parent, x)
#     y = find(parent, y)

#     parent[max(x,y)] = min(x,y)
#     return parent

# cost = 0
# for _ in range(E) :
#     c, x, y = heapq.heappop(edge)
#     if find(parent,x) == find(parent, y) :
#         continue
#     parent = union(parent, x,y)
#     cost += c









# 예시 코드

# import sys

# v, e = map(int, input().split())
# # 부모 테이블 초기화
# parent = [0] * (v+1)
# for i in range(1, v+1):
#     parent[i] = i

# # find 연산
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# # union 연산
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# # 간선 정보 담을 리스트와 최소 신장 트리 계산 변수 정의
# edges = []
# total_cost = 0

# # 간선 정보 주어지고 비용을 기준으로 정렬
# for _ in range(e):
#     a, b, cost = map(int, input().split())
#     edges.append((cost, a, b))

# # 간선 정보 비용 기준으로 오름차순 정렬
# edges.sort()

# # 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
# for i in range(e):
#     cost, a, b = edges[i]
#     # find 연산 후, 부모노드 다르면 사이클 발생 X으므로 union 연산 수행 -> 최소 신장 트리에 포함!
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         total_cost += cost
# print(parent)
# print(total_cost)