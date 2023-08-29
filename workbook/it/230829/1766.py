import sys
import heapq

def solution():
    
    n, m = map(int,input().split())

    depth = [0]*(n+1)
    heap = []
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        depth[b] += 1

    for i in range(1,n+1):
        if depth[i] == 0:
            heapq.heappush(heap, i)
    
    while heap:
        target = heapq.heappop(heap)

        for next in graph[target]:
            depth[next] -= 1
            if depth[next] == 0:
                heapq.heappush(heap, next)
        print(target, end=" ")
            


if __name__ == "__main__" :
    input = sys.stdin.readline


    solution()


# import sys
# import heapq

# def solution():
    
#     n, m = map(int,input().split())

#     parents = [i for i in range(n+1)]
#     heap = []
#     depth = 0

#     def find(a):
#         nonlocal depth
#         routes = [a]
        
#         while routes[-1] != parents[routes[-1]]:
#             routes.append(parents[routes[-1]])
                
#         while routes:
#             target  = routes.pop()
#             heapq.heappush(heap, (depth, target))
#             parents[target] = 0
#             depth += 1
            

#     for _ in range(m):
#         a,b = map(int,input().split())
#         parents[b] = a
#     for i in range(1,n+1):
#         if parents[i] == 0:
#             continue
#         find(i)


#     while heap:
#         print(heapq.heappop(heap)[1], end=" ")
            


# if __name__ == "__main__" :
#     input = sys.stdin.readline


#     solution()
