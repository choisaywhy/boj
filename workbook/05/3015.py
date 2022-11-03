import sys 
from collections import deque

input = sys.stdin.readline
N = int(input())
heights = [int(input()) for _ in range(N)]
stack = deque()
res = 0

for i in range(N-1,-1,-1) :
    eql = 0
    while stack and heights[stack[-1]] <= heights[i] :
        if heights[stack[-1]] == heights[i] :
            eql += 1
        else :
            res += 1
        stack.pop()

    if eql :
        res += eql
        if stack :
            res += 1
        for _ in range(eql) : # 요 작업을 아예 함께 넘겨주는 방식 (by others)
            stack.append(i)
    elif not eql and stack : # 옆에 있는 노드와는 무조건 쌍을 이룸
        res += 1
    stack.append(i)
print(res)



# import sys 
# from collections import deque

# input = sys.stdin.readline
# N = int(input())
# heights = [int(input()) for _ in range(N)]
# stack = deque()
# res = 0

# for i in range(N-1,-1,-1) :
#     eql = 0
#     print('i',i,'heights',heights[i])
#     while stack and heights[stack[-1]] <= heights[i] :
#         if heights[stack[-1]] == heights[i] :
#             eql += 1
#         else :
#             res += 1
#         stack.pop()

#     if eql :
#         res += eql
#         if stack :
#             res += 1
#         for _ in range(eql) :
#             stack.append(i)
#     elif not eql and stack : # 옆에 있는 노드와는 무조건 쌍을 이룸
#         res += 1

#     print(res,'res', eql, 'eql')


#     stack.append(i)
#     print(stack,'stack')
# print(res)
