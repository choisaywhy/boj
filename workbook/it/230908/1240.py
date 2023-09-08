import sys
from collections import deque
def solution():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]


    def bfs(start, end):
        queue = deque([(start,0)])
        visited = [False]*(n+1)
        visited[start] = True

        while queue:
            node, d = queue.popleft()

            for next, dist in graph[node]:
                if visited[next]:
                    continue
                
                if next == end:
                    return d+dist

                visited[next] = True
                queue.append((next,d+dist))



    for _ in range(n-1):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    for _ in range(m):
        a,b = map(int,input().split())
        print(bfs(a,b))

    


if __name__ == "__main__" :
    input = sys.stdin.readline

    solution()




# import sys
# def solution():
#     n,m = map(int,input().split())
#     cost = [[1e9]*(n+1) for _ in range(n+1)]

#     for _ in range(n-1):
#         a,b,c = map(int,input().split())
#         cost[a][b] = c
#         cost[b][a] = c
#     for i in range(1,n+1):
#         cost[i][i] = 0
    
#     for k in range(1,n+1):
#         for i in range(1,n+1):
#             for j in range(1,n+1):
#                 if cost[i][j] <= cost[i][k]+cost[k][j]:
#                     continue
#                 cost[i][j] = cost[i][k]+cost[k][j]
    
#     for _ in range(m):
#         a,b = map(int,input().split())
#         print(cost[a][b])

# if __name__ == "__main__" :
#     input = sys.stdin.readline

#     solution()



# import sys
# def solution():
#     n,m = map(int,input().split())
#     parents = [i for i in range(n+1)]
#     graph = {}

#     def find(a,parents):
#         if parents[a] != a:
#             parents[a] = find(parents[a],parents)
#         return parents[a]
    
#     def union(a,b,parents):
#         ap,bp = find(a,parents), find(b,parents)

#         parents[max(ap,bp)] = min(ap,bp)
#         return parents
    
    

#     for _ in range(n-1):
#         a,b,dist = map(int,input().split())
#         graph[a] = graph.get(a,[]) + [(b,dist)]
#         graph[b] = graph.get(b,[]) + [(a,dist)]

#         parents = union(a,b,parents)
    
#     root = 0
    
#     for node in range(1,n+1):
#         if parents[node] == node:
#             root = node
#         else:
#             parents[node] = find(node,parents)
    
    


# if __name__ == "__main__" :
#     input = sys.stdin.readline

#     solution()
