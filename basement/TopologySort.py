import sys
from collections import deque
input = sys.stdin.readline

def topologySort(V, E) :

    in_degree = [0] * (V+1)
    graph = [[] for _ in range(V+1)]
    ans = []
    queue = deque()

    for _ in range(E) :
        x, y = map(int, input().split()) # 두 정점 x, y에 대해 x->y가 자명함
        graph[x].append(y)
        in_degree[y] += 1 # 진입 차수 저장

    for i in range(1, V+1) :
        if in_degree[i] == 0 : # 진입 차수가 0인 정점을 queue에 저장
            queue.append(i)
    
    while queue :
        node = queue.popleft()
        ans.append(node)

        for next in graph[node] : # 진입 차수가 0인 정점 node를 삭제하며, 이와 연결된 next에 반영
            in_degree[next] -= 1
            if in_degree[next] == 0 : # node가 삭제된 새로운 그래프에서 next의 진입 차수가 0인 경우
                queue.append(next) # queue에 삽입
    
    if len(ans) < V : # 모든 노드를 순회하지 못한 경우
        print('해당 그래프에 사이클이 존재하여 위상정렬을 진행할 수 없습니다.')
    else :
        print(*ans)

 
V, E = map(int, input().split()) # V = vertex 수, E = edge 수


topologySort(V, E)