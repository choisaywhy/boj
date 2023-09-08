import sys
def solution():
    s,c = map(int,input().split())
    so = [int(input()) for _ in range(s)]

    start = 1
    end = max(so)
    mid = (start+end)//2

    while start <= end:
        count = 0

        for springonion in so:
            count += springonion // mid
        
        if count < c:
            end = mid - 1
        else:
            start = mid + 1
            
        mid = (start+end)//2

    print(sum(so)-mid*c)        


if __name__ == "__main__" :
    input = sys.stdin.readline

    solution()
