import sys
import heapq
def solution():
    n,c = map(int,input().split())
    mes = list(map(int,input().split()))
    order = {}
    count = {}
    heap = []

    for i in range(n):
        order[mes[i]] = order.get(mes[i],i)
        count[mes[i]] = count.get(mes[i],0) + 1
    
    for i in list(set(mes)):
        heapq.heappush(heap, (-count[i], order[i],i))

    while heap:
        x,y,z = heapq.heappop(heap)
        for _ in range(-x):
            print(z,end=" ")


if __name__ == "__main__" :
    input = sys.stdin.readline

    solution()



# import sys
# import heapq
# def solution():
#     n,c = map(int,input().split())
#     mes = list(map(int,input().split()))
#     order = [-1]*(c+1)
#     count = [0]*(c+1)
#     heap = []

#     for i in range(n):
#         if order[mes[i]] == -1:
#             order[mes[i]] = i
#         count[mes[i]] += 1
    
#     for i in list(set(mes)):
#         heapq.heappush(heap, (-count[i], order[i],i))

#     while heap:
#         x,y,z = heapq.heappop(heap)
#         for _ in range(-x):
#             print(z,end=" ")


# if __name__ == "__main__" :
#     input = sys.stdin.readline

#     solution()
