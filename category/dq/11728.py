import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = A + B
answer.sort()

for a in answer :
    print(a, end=" ")



# import sys
# from collections import deque

# input = sys.stdin.readline

# N, M = map(int,input().split())
# A = deque(map(int, input().split()))
# B = deque(map(int, input().split()))

# answer = []

# for b in B :
#     pointer = 0
#     while True : # 현재 b 해결
#         if b < A[pointer] :
#             for _ in range(pointer):
#                 answer.append(A.popleft())
#             answer.append(b)
#             break
#         elif b > A[pointer] :
#             pointer += 1
#         if pointer >= len(A) :
#             answer.extend(A)
#             answer.append(b)
#             break
# answer.extend(A)

# for a in answer :
#     print(a, end=" ")