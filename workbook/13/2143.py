import sys
from bisect import *

def solution(t,n,a,m,b):
    suba, subb = [],[]

    for i in range(n):
        for j in range(i,n):
            suba.append(sum(a[i:j+1]))
    for i in range(m):
        for j in range(i,m):
            subb.append(sum(b[i:j+1]))
    
    subb.sort()
    ans = 0
    
    for sa in suba:
        start, end = bisect_left(subb, t-sa), bisect_right(subb, t-sa)
        ans += end - start
    
    print(ans)



            




if __name__ == "__main__" :
    input = sys.stdin.readline
    t = int(input())
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    solution(t,n,a,m,b)