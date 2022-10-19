# https://www.acmicpc.net/workbook/view/7287

import sys
from collections import Counter

input = sys.stdin.readline

array1 = Counter(str(input().strip()))
array2 = Counter(str(input().strip()))


for key in list(set(array1.keys())&set(array2.keys())) :
    num = min(array1[key], array2[key])
    array1[key] -= num
    array2[key] -= num

count = sum(array1.values()) +sum(array2.values())
print(count)
