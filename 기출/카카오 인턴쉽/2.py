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
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER x
#

def solution(cost, x):
    answer = 0    
    for i in range(len(cost)-1, -1, -1) :
        if cost == 0 :
            break
        if cost[i] > x :
            continue
        answer += 2**i
        x -= cost[i]
    return answer % (10**9 + 7)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    cost_count = int(input().strip())

    cost = []

    for _ in range(cost_count):
        cost_item = int(input().strip())
        cost.append(cost_item)

    x = int(input().strip())

    result = solution(cost, x)

    fptr.write(str(result) + '\n')

    fptr.close()
