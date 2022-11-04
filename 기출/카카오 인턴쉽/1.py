
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
#  1. INTEGER x
#  2. INTEGER y
#  3. INTEGER z
#

def solution(x, y, z):
    if abs(x-y) > z :
        return -1
    
    k = 0
    if x > y :
        k = (z - (x - y)) //2 + x
    elif x < y :
        k = (z - (y - x)) //2 + y
    else :
        k = z // 2 + x
    return k
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = int(input().strip())

    y = int(input().strip())

    z = int(input().strip())

    result = solution(x, y, z)

    fptr.write(str(result) + '\n')

    fptr.close()
