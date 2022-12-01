import sys


input = sys.stdin.readline
N, M = map(int,input().split())
trees = list(map(int,input().split()))


mid = 0
start = 0
end = max(trees)

while start <= end :
    length = 0
    mid = (start + end) // 2

    for tree in trees :
        if tree - mid <= 0 :
            continue
        length += tree - mid
    
    if length >= M :
        start = mid + 1
    else :
        end = mid - 1
    
print(end)
    
