# https://www.acmicpc.net/workbook/view/7289

import sys

input = sys.stdin.readline

N = int(input())
tops = list(map(int,input().split()))








# 시간 초과 -> O(N**2)
# answer = []

# for h in range(N) :
#     for i in range(h-1, -1, -1) :
#         if tops[h] <= tops[i] :
#             answer.append(i+1)
#             break
#     if len(answer) != h+1 :
#         answer.append(0)

# for an in answer :
#     print(an, end=' ')