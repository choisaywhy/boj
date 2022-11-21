import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))
deq = deque()

for i in range(N) :
    while deq and deq[-1][0] >= A[i]:
        deq.pop()
    # while이 끝나는 경우는 나보다 작은 값을 만났을 때
    
    while deq and deq[0][0] < A[i] and deq[0][1] < i - L + 1 :
        deq.popleft()
    
    deq.append((A[i], i))
    print(deq[0][0], end = " ")


# debegging
# import sys
# from collections import deque

# input = sys.stdin.readline

# N, L = map(int, input().split())
# A = list(map(int, input().split()))
# D = []
# stack = []

# for i in range(N) :
#     print(A[i],i, 'turn')
#     while stack and stack[-1][0] >= A[i] :
#         print(stack[-1],'은 나보다 큼')
#         stack.pop()
#         print(stack,'updated')
#     # while이 끝나는 경우는 나보다 작은 값을 만났을 때
    
#     if stack and stack[-1][0] < A[i] :
#         if stack[-1][1] < i - L + 1 :
#             print(stack[-1],'이미 지난 index')
#             stack.pop()
#             print(stack,'updated')
#         else :
#             print(stack[-1],'범위 안의 index')
#             print(stack[0][0])
#             stack.append((A[i], i))
#             print(stack,'updated')
#             continue
    
#     if not stack :
#         print('nothing in stack')
#         stack.append((A[i], i))
#         print(stack[-1][0])

