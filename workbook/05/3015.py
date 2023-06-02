# 230602 2차 풀이
import sys

def solution(N, heights):

    stack = []
    pair = 0

    for h in heights:
        while stack and stack[-1][0] < h:
            pair += stack.pop()[1] # 오른쪽 기준 왼쪽 쌍 더하기
    
        if not stack:
            stack.append((h,1))
            continue
        
        if stack[-1][0] != h:
            stack.append((h,1))
            pair += 1
        else:
            eql = stack.pop()[1]
            pair += eql
            if stack:
                pair += 1
            stack.append((h, eql+1))


    print(pair)
        


if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    heights = [int(input()) for _ in range(N)]
    solution(N, heights)





# 1차 정답
# import sys 
# from collections import deque

# input = sys.stdin.readline
# N = int(input())
# heights = [int(input()) for _ in range(N)]
# stack = deque()
# res = 0

# for i in range(N-1,-1,-1) :
#     eql = 0

#     while stack and heights[stack[-1][0]] < heights[i] :
#         res += stack.pop()[1]
    
#     if not stack :
#         stack.append((i, 1))
#         continue

#     if heights[stack[-1][0]] == heights[i] :
#         eql = stack.pop()[1]
#         res += eql
#         if stack :
#             res+=1
#         stack.append((i, eql + 1))
#     else :
#         stack.append((i, 1))
#         res += 1

# print(res)




# import sys 
# from collections import deque

# input = sys.stdin.readline
# N = int(input())
# heights = [int(input()) for _ in range(N)]
# stack = deque()
# res = 0

# for i in range(N-1,-1,-1) :
#     eql = 0

#     while stack and heights[stack[-1][0]] < heights[i] :
#         res += 1
#         stack.pop()

#     if stack :
#         res += 1
#         if heights[stack[-1][0]] == heights[i] :
#             eql = stack.pop()[1]
#             res += eql

#     if eql :
#         stack.append((i, eql + 1))
#     else :
#         stack.append((i, 1))


# print(res)




# import sys 
# from collections import deque

# input = sys.stdin.readline
# N = int(input().strip())
# heights = [int(input()) for _ in range(N)]
# stack = deque()
# res = 0

# for i in range(N-1,-1,-1) :
#     eql = 0
#     while stack and heights[stack[-1]] <= heights[i] :
#         if heights[stack[-1]] == heights[i] :
#             eql += 1
#         else :
#             res += 1
#         stack.pop()
#     if stack :
#         res += 1

#     if eql :
#         res += eql
#         for _ in range(eql) : # 요 작업을 아예 함께 넘겨주는 방식 (by others) -> 해당 시퀀스에서 시간초과 가능성 농후,
#             stack.append(i)   # stack 안에 eql 값을 저장 할 다른 방법 필요

#     stack.append(i)
# print(res)



# import sys 
# from collections import deque

# input = sys.stdin.readline
# N = int(input())
# heights = [int(input()) for _ in range(N)]
# stack = deque()
# res = 0

# for i in range(N-1,-1,-1) :
#     eql = 0
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
#         for _ in range(eql) : # 요 작업을 아예 함께 넘겨주는 방식 (by others)
#             stack.append(i)
#     elif not eql and stack : # 옆에 있는 노드와는 무조건 쌍을 이룸
#         res += 1
#     stack.append(i)
# print(res)



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



# import sys 
# from collections import deque

# input = sys.stdin.readline
# N = int(input())
# heights = [int(input()) for _ in range(N)]
# stack = deque()
# res = 0

# for i in range(N-1,-1,-1) :
#     flag = False
#     while stack and heights[stack[-1]] <= heights[i] :
#         stack.pop()
#         flag = True
#     if stack :
#         res += stack[-1] - i
#     elif not stack and flag :
#         res += N - (i+1)

#     stack.append(i)
# print(res)
