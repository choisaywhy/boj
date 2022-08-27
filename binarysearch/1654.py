import sys


input = sys.stdin.readline
K, N = map(int,input().split())
lan = []

for _ in range(K):
    lan.append(int(input()))

lan.sort()

mid = 0
start = 1
end = lan[-1]

while start <= end :
    count = 0
    mid = (start + end) // 2

    for l in lan :
        count += l // mid
    
    if count < N :
        end = mid - 1
    else :
        start = mid + 1
    
print(end)
    
