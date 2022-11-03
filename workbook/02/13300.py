# https://www.acmicpc.net/workbook/view/7287

import sys
from collections import Counter
input = sys.stdin.readline

N, K = map(int, input().split())
room = 0
# dict = {str(grade)+str(gender) : 0 for grade in range(1,7) for gender in range(2)} # key = 학년 + 성별, value = 명 수
dict = {}
for _ in range(N) : 
    key = "".join(map(str, input().strip().split()))
    dict[key] = dict.get(key,0) + 1
for num in dict.values() :
    room += num // K 
    if num % K :
        room += 1

print(room)