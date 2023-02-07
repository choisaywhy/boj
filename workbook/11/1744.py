import sys
from collections import deque


def solution(N, arr) :
    arr.sort()
    ans = 0
    flag = True

    while len(arr) > 1 :
        a = arr.pop()
        b = arr.pop()

        if flag and a < 0 and b < 0 :
            flag = False
            arr.extend([a,b])
            arr.sort(reverse=True)
            continue

        if a + b > a * b :
            ans += a
            arr.append(b)
        else :
            ans += a * b
    
    if arr :
        ans += arr.pop()

    print(ans)

if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    arr = [int(input()) for _ in range(N)]

    solution(N, arr)



# debugging
# import sys
# from collections import deque


# def solution(N, arr) :
#     arr.sort()
#     ans = 0
#     flag = True

#     while len(arr) > 1 :
#         a = arr.pop()
#         b = arr.pop()

#         print(a,b,"turn")
#         if flag and a < 0 and b < 0 :
#             print("음수 진입, reversed")
#             flag = False
#             arr.extend([a,b])
#             arr.sort(reverse=True)
#             print(arr,"updated")
#             continue

#         if a + b > a * b :
#             print(a,"더하기")
#             ans += a
#             arr.append(b)
#         else :
#             print(a,"*",b)
#             ans += a * b
    
#     if arr :
#         ans += arr.pop()

#     print(ans)

# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N = int(input())
#     arr = [int(input()) for _ in range(N)]

#     solution(N, arr)


# def solution(N, arr) :
#     arr.sort()
#     ans = 0

#     while len(arr) > 1 :
#         a = arr.pop()
#         b = arr.pop()

#         if a * b > 0 :
#             print(a,"*",b)
#             ans += a * b
#         elif a * b == 0 :
#             if a <= 0 and b <= 0 :
#                 print(a,"*",b)
#                 pass
#             else : # b = 0, a는 양수
#                 ans += a + b
#                 if arr :
#                     arr.append(0)
#             arr.sort(reverse=True)
#         else :
#             print(a,b,"띠로")
#             ans += a + b

#     if arr :
#         print("남은거",arr[-1])
#         ans += arr.pop()

#     print(ans)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N = int(input())
#     arr = [int(input()) for _ in range(N)]

#     solution(N, arr)
