# https://www.acmicpc.net/workbook/view/7287

import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())

for _ in range(N) :
    flag = False
    array1, array2 = map(str, input().strip().split())
    dict1 = Counter(array1)
    dict2 = Counter(array2)
    if dict1 != dict2 :
        print("Impossible")
    else :
        print("Possible")
    