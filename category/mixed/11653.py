# import sys
# from math import sqrt


# def is_primary(N:int)->list:
#     primary = [True] * (N + 1)
#     primary[0], primary[1] = False, False

#     for i in range(2, int(sqrt(N))+1):
#         if primary[i] :
#             j = 2
#             while i*j <= N:
#                 primary[i*j] = False
#                 j += 1
#     return primary

# def factorization(N:int):
#     primary = is_primary(N)
#     if primary[N]:
#         print(N)
#         return

#     for p in range(2,int(sqrt(N))+1):
#         if primary[p] :
#             while not N % p and N:
#                 print(p)
#                 N //= p
#         if not N :
#             break
        

# N = int(sys.stdin.readline())
# factorization(N)


import sys
from math import sqrt

def factorization(N:int):

    for p in range(2,N+1):
        while not N % p and N:
            print(p)
            N //= p
        if not N :
            return
        

N = int(sys.stdin.readline())
factorization(N)
