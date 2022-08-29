from calendar import c
from multiprocessing import heap
import sys
import heapq 

input = sys.stdin.readline

N = int(input())
arr = []

for i in range(1,N+1):
    arr.append(int(input()))
    heap = arr[:]
    heapq.heapify(heap)
    if i <= 2:
        print('answer',heapq.heappop(heap))
        continue

    for _ in range(i//2 + i%2):
        print('before answer',heapq.heappop(heap)   )
        # heapq.heappop(heap)        
    print('answer',heapq.heappop(heap))
    

