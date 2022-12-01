# 9 out of 15 
# 6 time out

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY box as parameter.
#
def solution(box):
    new_max = box.index(max(box)) # max index값 
    while new_max != 0 :
        if max(box) - min(box) == 1:
            break
        x = box[new_max] - sum(box[:new_max+1]) // (new_max+1)  
        box[new_max-1] += x
        box[new_max] -= x
        new_max = box.index(max(box))
        
    return box[new_max]

# from heapq import heappush, heappop
# def solution(box):
#     minheap = []
#     maxheap = []
#     for i, b in enumerate(box) : 
#         heappush(minheap, (b, i))
#         heappush(maxheap, (-b, i))

#     temp = []
#     while minheap :
#         smb, smi = heappop(minheap)
#         lgb, lgi = heappop(maxheap)
#         lgb *= -1
        
#         if lgi == 0 or smb > lgb:
#             break
        
#         if smi > lgi :
#             temp.append((smb, smi))
#             heappush(maxheap, (-lgb, lgi))
#             continue
        
#         x = lgb - (lgb + smb) // 2
#         box[smi] += x
#         box[lgi] -= x
#         heappush(minheap, (box[smi], smi))
#         heappush(maxheap, (-box[smi], smi))
#         heappush(minheap, (box[lgi], lgi))
#         heappush(maxheap, (-box[lgi], lgi))
        
#         if temp :
#             for t in temp :
#                 heappush(minheap, t)
#             temp = []

#     return heappop(maxheap)[0] * -1




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    box_count = int(input().strip())

    box = []

    for _ in range(box_count):
        box_item = int(input().strip())
        box.append(box_item)

    result = solution(box)

    fptr.write(str(result) + '\n')

    fptr.close()
