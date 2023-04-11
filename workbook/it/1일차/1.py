import sys

def solution(h,w,n,m):
    c = w // (m+1)
    r = h // (n+1)
    if w % (m+1):
        c += 1
    if h % (n+1):
        r += 1
    print(c*r)
    




if __name__ == "__main__" :
    input = sys.stdin.readline
    h,w,n,m = map(int, input().split())
    solution(h,w,n,m)