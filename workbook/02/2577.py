# https://www.acmicpc.net/workbook/view/7287

import sys
from collections import Counter
input = sys.stdin.readline

mul = 1
for _ in range(3) :
    mul *= int(input())
hash = Counter(str(mul))
for i in range(10):
    print(hash[str(i)])
