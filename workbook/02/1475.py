# https://www.acmicpc.net/workbook/by/BaaaaaaaaaaarkingDog
import sys
from collections import Counter
input = sys.stdin.readline

num = str(input().strip())
dict = Counter(num)

sum = dict['6'] + dict['9']
dict['6'] = sum // 2
dict['9'] = sum - dict['6']

print(max(dict.values()))