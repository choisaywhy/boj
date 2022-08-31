import sys
import heapq 

input = sys.stdin.readline

N = int(input())
minHeap = []
maxHeap = []

for _ in range(N):
    num = int(input())

    if len(maxHeap) and -1 * maxHeap[0] >= num :
        heapq.heappush(maxHeap, -1 * num)
    else :
        heapq.heappush(minHeap, num)
    
    if len(minHeap) - len(maxHeap) > 2 :
        heapq.heappush(maxHeap, -1 * heapq.heappop(minHeap))
    elif not len(minHeap) - len(maxHeap) :
        heapq.heappush(minHeap, -1 * heapq.heappop(maxHeap))
    print(minHeap[0])

# import sys
# import heapq 

# input = sys.stdin.readline

# N = int(input())
# heap = []
# heapq.heapify(heap)
# for i in range(N):

#     heapq.heappush(heap,int(input()))

#     print(heapq.nsmallest(n=i//2+1, iterable = heap)[-1]) # 결국엔 sort연산
    




# import sys
# import heapq 

# input = sys.stdin.readline

# N = int(input())
# arr = []

# for i in range(N):
#     arr.append(int(input()))
#     heap = arr[:] ## 이곳에서 시간 초과>??
#     heapq.heapify(heap)
#     if not i :
#         print(heapq.heappop(heap))
#         continue

#     for _ in range(i//2):
#         heapq.heappop(heap)        
#     print(heapq.heappop(heap))
    

