import sys
from collections import defaultdict
def solution():
    n = int(input())
    a,b,c,d = [0]*n,[0]*n,[0]*n,[0]*n

    for i in range(n):
        tmp = list(map(int,input().split()))
        a[i] = tmp[0]
        b[i] = tmp[1]
        c[i] = tmp[2]
        d[i] = tmp[3]

    ab = defaultdict(int)
    for i in range(n):
        for j in range(n):
            ab[a[i]+b[j]] += 1
            
    ans = 0
    for i in range(n):
        for j in range(n):
            if -(c[i]+d[j]) in ab:
                ans += ab[-(c[i]+d[j])]
    
    print(ans)
    

if __name__ == "__main__" :
    input = sys.stdin.readline


    solution()



# import sys
# def solution():
#     n = int(input())
#     a,b,c,d = [0]*n,[0]*n,[0]*n,[0]*n

#     for i in range(n):
#         tmp = list(map(int,input().split()))
#         a[i] = tmp[0]
#         b[i] = tmp[1]
#         c[i] = tmp[2]
#         d[i] = tmp[3]
    
#     a.sort()
#     b.sort()
#     c.sort()
#     d.sort()

#     print(a,b,c,d)

    

# if __name__ == "__main__" :
#     input = sys.stdin.readline


#     solution()
