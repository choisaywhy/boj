import sys
import heapq as hq

input = sys.stdin.readline
max_heap = []
min_heap = []

N = int(input())
middle = 0

for _ in range(N):
    num = int(input())
    if num < middle :
        hq.heappush(max_heap, -num)
    else :
        hq.heappush(min_heap, num)
    
    if len(max_heap) < len(min_heap) :
        hq.heappush(max_heap, hq.heappop(min_heap)*-1)
    elif len(max_heap) > len(min_heap) + 1 :
        hq.heappush(min_heap, hq.heappop(max_heap)*-1)

    middle = max_heap[0] * -1
    print(middle)


