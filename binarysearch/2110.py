import sys


input = sys.stdin.readline

N, C = map(int,input().split())
house = [int(input()) for _ in range(N)]

house.sort()

start = 1
end = house[-1] - house[0]
mid = 0


while start <= end :
    router = 0
    mid = (start + end) // 2
    temp = 0

    for h in house :
        if h >= temp :
            router += 1
            temp = h + mid 
    
    if router < C :
        end = mid -1
    else :
        start = mid + 1

print(end)

