# original hanoi completed
# ver 2,3 have to be done 
import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())

def hanoi(N, start, end) :
    global tops
    global K

    if K < 1 :
        return

    if N == 1:
        if K >= 1 :
            tops[end].append(tops[start].pop())
            K -= 1
        return

    hanoi(N-1, start, 3-start-end)
    if K >= 1 :
        tops[end].append(tops[start].pop()) 
        K -= 1
    hanoi(N-1, 3-start-end, end)

def hanoi2(N, start, end) :
    global tops
    global K

    if K < 1 :
        return

    if N == 1:
        if K >= 1 :
            tops[end].append(tops[start].pop())
            K -= 1
        return

    hanoi(N-1, start, 3-start-end)
    if K >= 1 :
        tops[end].append(tops[start].pop()) 
        K -= 1
    hanoi(N-1, 3-start-end, end)


tops = [deque([i for i in range(N-1,-1,-1)]),deque(),deque()]

if M == 1:
    hanoi(N, 0, 2)
elif M == 2 :
    hanoi2(N, 0, 2)
elif M == 3 :
    pass

result = [0 for _ in range(N)]
for i in range(3) :
    while tops[i] :
        result[tops[i].pop()] = str(i + 1)
print(" ".join(result))



# trial 2 문제 해결
# import sys
# from collections import deque

# input = sys.stdin.readline

# M, N, K = map(int, input().split())

# def hanoi(N, start, end) :
#     global tops
#     global K

#     if K < 1 :
#         return

#     if N == 1:
#         if K >= 1 :
#             tops[end].append(tops[start].pop())
#             K -= 1
#         return

#     hanoi(N-1, start, 3-start-end)
#     if K >= 1 :
#         tops[end].append(tops[start].pop()) # problem, if K < 1 의 영향력이 닫지 않음
#         K -= 1
#     hanoi(N-1, 3-start-end, end)



# tops = [deque([i for i in range(N-1,-1,-1)]),deque(),deque()]

# if M == 1:
#     hanoi(N, 0, 2)
#     print(tops)




# 1st trial
# import sys

# input = sys.stdin.readline

# M, N, K = map(int, input().split())

# def hanoi(N, start, end) : # N: 원판 개수, K: 제한 시간
#     global K
#     K -= 1
#     if K == 0 :
#         for i in range(3) :
#             while tops[i] :
#                 temp = tops[i].pop()
#                 print('temp',temp,'i',i)
#                 result[temp] = str(i)
#         return
#     if N == 1 :
#         if tops[start] :
#             tops[end].append(tops[start].pop())
#         return
    

#     hanoi(N-1,start,3-start-end)
#     if tops[start]:
#         tops[end].append(tops[start].pop())
#     hanoi(N-1,3-start-end,end)

# def hanoi3(N,K) :
#     pass
# def hanoi4(N,K) :
#     pass


# tops = [[i for i in range(N-1,-1,-1)], [], []]
# result = [0 for _ in range(N)]

# if M == 1:
#     hanoi(N,0,2) 
# elif M == 2:
#     hanoi3(N,K)
# elif M == 3:
#     hanoi4(N,K)

# print(" ".join(result))
