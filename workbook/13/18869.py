import sys
from collections import defaultdict as dd

def solution(m,n,planets):
    universe = dd(int)
    pair = 0

    for planet in planets:
        tmp = sorted(list(set(planet)))
        ranks = {tmp[i]:i for i in range(len(tmp))}
        universe[tuple([ranks[x] for x in planet])] += 1
    

    for cnt in universe.values():
        pair += cnt * (cnt - 1) // 2

    print(pair)
        
        


if __name__ == "__main__" :
    input = sys.stdin.readline
    m,n = map(int, input().split())
    planets = [list(map(int, input().split())) for _ in range(m)]
    solution(m,n,planets)

# 시간초과
# debugging ver
# import sys

# def solution(m,n,planet):
#     pair = 0
#     for i in range(m-1): # a
#         a = []
#         for idx, v in enumerate(planet[i]):
#             a.append((v,idx))
#         a.sort()
        
#         for j in range(i+1,m): # b
#             flag = True
#             for k in range(n-1):
#                 v1, idx1 = a[k]
#                 v2, idx2 = a[k+1]

#                 print(planet[j], idx1,idx2, v1, v2)
                
#                 if v1 == v2:
#                     if planet[j][idx1] != planet[j][idx2]:
#                         flag = False
#                         break
#                 else: # v1 < v2
#                     if planet[j][idx1] >= planet[j][idx2]:
#                         flag = False
#                         break
#             if flag:
#                 pair += 1
                
#     print(pair)

            




# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     m,n = map(int, input().split())
#     planet = [list(map(int, input().split())) for _ in range(m)]
#     solution(m,n,planet)