# https://www.acmicpc.net/workbook/view/7287

import sys

input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
v = int(input())

print(array.count(v))