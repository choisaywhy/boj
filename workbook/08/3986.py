# 반례 없는 제대로된 방식을 고안하면 됨
import sys

def solution(N, words):
    count = 0
    for word in words :
        stack = []
        for w in word :
            if stack and w == stack[-1] :
                stack.pop()
                continue
            stack.append(w)
                
        if not stack :
            count += 1
    print(count)


if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    words = [str(input().strip()) for _ in range(N)]
    solution(N, words)
    


# first trial 
# counter example BABBAB
# import sys
# import re

# def solution(N, words):
#     count = 0
#     for word in words :
#         stack = []
#         flag = True
#         for w in word :
#             if not stack or w not in stack:
#                 stack.append(w)
#                 continue
#             if w == "A" :
#                 if stack.pop() != 'A' :
#                     flag = False
#                     break
#             elif w == "B" :
#                 if stack.pop() != 'B' :
#                     flag = False
#                     break
#         if flag and not stack :
#             count += 1
#     print(count)


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N = int(input())
#     words = [str(input().strip()) for _ in range(N)]
#     solution(N, words)
    