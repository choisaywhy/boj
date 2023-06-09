import sys

def solution(n,a):
    
    start = 0
    end = n-1
    ans = 1e14
    while start < end:

        mixed = a[start] + a[end]
        if abs(ans) > abs(mixed):
            ans = mixed

        
        if mixed < 0:
            start += 1
        elif mixed > 0:
            end -= 1
        else:
            break
    
    print(ans)




if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int,input().split()))
    solution(n,a)