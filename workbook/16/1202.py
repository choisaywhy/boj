import sys
from heapq import *

def solution(n,k,j,b):
    ans = 0
    b.sort()

    available = []

    for bag in b:
        while j and bag >= j[0][0]:
            w, v = heappop(j)
            heappush(available, -v)
        
        if available:
            ans -= heappop(available)
        elif not j:
            break

    print(ans)



if __name__ == "__main__" :
    input = sys.stdin.readline
    n,k = map(int,input().split())

    j = []
    for _ in range(n):
        heappush(j,tuple(map(int,input().split())))
    b = [int(input()) for _ in range(k)]
    solution(n,k,j,b)



# 1st trial 시간초괴
# import sys
# from heapq import *

# def solution(n,k,j,b):
#     cost = 0

#     for m,v in j:
#         tmp = []

#         while b:
#             bag = heappop(b)
#             if m > bag:
#                 tmp.append(bag)
#                 continue
#             cost += v
#             break

#         while tmp:
#             heappush(b, tmp.pop())

#         if not b:
#             break
#     print(cost)

    

# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n,k = map(int,input().split())
#     j = [tuple(map(int,input().split())) for _ in range(n)]
#     j.sort(key=lambda x: x[1], reverse=True) # 보석 가격을 기준으로 sort
#     b = []
#     for _ in range(k):
#         heappush(b, int(input()))
#     solution(n,k,j,b)