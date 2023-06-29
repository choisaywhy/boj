# 구간합 logn

import sys
input = sys.stdin.readline

# Segment Tree 생성
def init(node, left, right) :
    if left == right:
        st[node] = A[left]
        return st[node]
    mid = left + (right - left) // 2
    st[node] = init(node*2, left, mid) + init(node*2+1, mid+1, right)

    return st[node]

# Segment Tree 탐색하여 구간 (left, right)의 구간 합 구하기
def search(node, start, end, left, right):
    if left > end or right < start: # out of range
        return 0
    if left <= start and end <= right:
        return st[node]
    
    mid = left + (right - left) // 2
    return search(node*2, start, mid, left, right) + search(node*2+1, mid + 1, end, left, right)

# Segment Tree 중 수정 된 값 갱신
def update(node, start, end, index, diff):
    if index < start or index > end: # out of range
        return 
    st[node] += diff
    if start != end:
        mid = start + (end - start) // 2
        update(node*2, start, mid, index, diff)
        update(node*2+1, mid+1, end, index, diff)
    


n = int(input())
A = list(map(int, input().split())) # 구간합을 구할 배열
i,j = map(int,input().split()) # 구간합 범위
idx, val = map(int,input().split()) # 변경할 인덱스, 값

st = [0]*(2*n)



