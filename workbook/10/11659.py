import sys

def solution(n,m,a,q):
    a = [0] + a
    for i in range(1,n+1):
        a[i] += a[i-1]

    for i,j in q:
        print(a[j]-a[i-1])




if __name__ == "__main__" :
    input = sys.stdin.readline
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    q = [tuple(map(int,input().split())) for _ in range(m)]
    solution(n,m,a,q)
