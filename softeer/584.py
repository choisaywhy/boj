#GBC
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
limits = []
for _ in range(N):
    l, s = map(int,input().split())
    limits += [s]*(l)

target = 0
ans = 0
for _ in range(M):
    l, s = map(int, input().split())
    for i in range(target, target+l):
        if s - limits[i] <= ans:
            continue
        ans = s - limits[i]
    
    target += l

print(ans)