import sys

def solution(H, W, blocks):
    ans = 0

    for i in range(1, W-1):
        rain = min(max(blocks[:i]), max(blocks[i+1:]))
        if blocks[i] < rain:
            ans += rain - blocks[i]

    print(ans)

if __name__ == "__main__" :
    input = sys.stdin.readline
    H, W = map(int ,input().split())
    blocks = list(map(int, input().split()))
    solution(H, W, blocks)


# debugging ver
# import sys

# def solution(H, W, blocks):
#     stack = []
#     ans, between = 0, []

#     for i in range(W):
#         print(i,'번째',blocks[i],'turn')
#         if not stack and blocks[i] == 0:
#             continue
#         if not stack or stack[-1] > blocks[i]:
#             print('stack 순서대로')
#             stack.append(blocks[i])
#             print('stack updated',stack)
#             continue

#         while stack and stack[-1] < blocks[i]:
#             between.append(stack.pop())

#         if between:
#             print('between 생성')
#             stack.append(blocks[i])
#             print('stack updated',stack)
#             print('between',between)
#             print('between',between)
#             ans += stack[-1]*len(between) - sum(between)
#             print(ans,'ans 갱신')
#             between = []
#         print('최종',stack)
#     if stack and between:
#         print('남은 between 처리')
#         ans += (stack[0] - stack[1])* len(between) - sum(between)

#     print(ans)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     H, W = map(int ,input().split())
#     blocks = list(map(int, input().split()))
#     solution(H, W, blocks)


# first trial, stack은 단방향성 iter, 해당 문제는 양방향 이므로 다른 방식 고안
# import sys

# def solution(H, W, blocks):
#     stack = [blocks[0]]
#     ans, between = 0, []

#     for i in range(1,W):
#         print(i,'번째',blocks[i],'turn')
#         if not stack or stack[-1] > blocks[i]:
#             print('stack 순서대로')
#             stack.append(blocks[i])
#             print('stack updated',stack)
#             continue

#         print('between 생성')
#         while stack and stack[-1] <= blocks[i]:
#             if stack[-1] == blocks[i]:
#                 stack.pop()
#                 continue
#             between.append(stack.pop())

#         stack.append(blocks[i])
#         print('stack updated',stack)

#         print('between',between)
#         ans += stack[-1]*len(between) - sum(between)
#         print(ans,'ans 갱신')
#         between = []
    
#     if stack and between:
#         print('남은 between 처리')
#         ans += (stack[0] - stack[1])* len(between) - sum(between)


#     print(ans)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     H, W = map(int ,input().split())
#     blocks = list(map(int, input().split()))
#     solution(H, W, blocks)