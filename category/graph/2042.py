import sys

def solution(n,m,k,num,op):
    st = [0]*(4*n)
    
    def init(node, l, r):
        if l == r:
            st[node] = num[l]
            return st[node]

        mid = l + (r-l)//2

        st[node] = init(node*2, l, mid) + init(node*2+1, mid+1, r)
        return st[node]

    def search(node, s, e, l, r):
        if l > e or r < s:
            return 0
        if l <= s and e <= r:
            return st[node]
        mid = s + (e-s)//2
        return search(node*2, s, mid, l, r) + search(node*2+1, mid + 1, e, l, r)
    
    def update(node, s, e, idx, val) -> None:
        if idx < s or e < idx:
            return
        st[node] = val + st[node]
        if s != e:
            mid = s + (e-s)//2
            update(node*2, s, mid, idx, val)
            update(node*2+1, mid+1, e, idx, val)
    
    init(1, 0, n-1)
    for a,b,c in op:
        if a == 1:
            update(1, 0, n-1, b-1, c-num[b-1])
            num[b-1] = c
        else:
            print(search(1,0,n-1,b-1,c-1))



if __name__ == "__main__" :
    input = sys.stdin.readline
    n,m,k = map(int,input().split())
    num = [int(input()) for _ in range(n)]
    op = [tuple(map(int,input().split())) for _ in range(m+k)]
    solution(n,m,k,num,op)

    