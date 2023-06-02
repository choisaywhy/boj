import sys

def solution(N,M,A):
    
    A.sort()
    l, r = 0, 1
    ans = A[-1] - A[0]

    while l <= r and r < N and l < N:
        diff = abs(A[r] - A[l])
        if diff < M:
            r += 1
        else:
            ans = min(ans, diff)
            l += 1
            
    print(ans)




if __name__ == "__main__" :
    input = sys.stdin.readline
    N,M = map(int,input().split())
    A = [int(input()) for _ in range(N)]
    solution(N,M,A)