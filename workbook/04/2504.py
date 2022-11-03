# https://www.acmicpc.net/workbook/by/BaaaaaaaaaaarkingDog

import sys
from collections import deque


input = sys.stdin.readline

bk = str(input().strip())
stack = deque()
temp = 1
result = 0

for i in range(len(bk)) :
    if bk[i] == '(' :
        temp *= 2
        stack.append(bk[i])
    elif bk[i] == '[' :
        temp *= 3
        stack.append(bk[i])
    elif bk[i] == ')' :
        if not stack or stack[-1] == '[' :
            result = 0
            break
        if bk[i-1] == '(' :
            result += temp
        temp //= 2
        stack.pop()
    elif bk[i] == ']' :
        if not stack or stack[-1] == '(' :
            result = 0
            break
        if bk[i-1] == '[' :
            result += temp
        temp //= 3
        stack.pop()
if stack :
    result = 0
print(result)


# 1st trial

# input = sys.stdin.readline
# bracket = str(input().strip())
# queue = deque()
# answer = 0
# count = 0
# flag = False
# for b in bracket :
#     print(b,'turn')
#     if b == '[' or b == '(' :
#         print(b,'append part')
#         if flag :
#             answer += count
#             count = 0
#             flag = False
#             print('pop ended, answer updated to',answer)
#         queue.append(b)
#         print('queue updated to',queue)

#     elif b == ']' :
#         print('[ pop part')
#         if not queue or queue.pop() != '[' :
#             print('wrong brancket')
#             answer = 0
#             break
#         if flag :
#             print('pop doubled')
#             count *= 3
#             print('count updated',count)
#         else :
#             count += 3
#             print('first pop count updated',count)
#         flag = True
#     elif b == ')' :
#         if not queue or queue.pop() != '(' :
#             print('wrong brancket')
#             answer = 0
#             break
#         if flag :
#             print('pop doubled')
#             count *= 2
#             print('count updated',count)
#         else :
#             count += 2
#             print('first pop count updated',count)
#         flag = True
# print(answer)