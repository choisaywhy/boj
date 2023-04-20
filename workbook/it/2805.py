import sys

def solution(N,M,tree):

    lo = 0
    hi = max(tree)

    while lo <= hi:
        mid = (lo + hi) // 2

        ans = 0
        for t in tree:
            if t - mid <= 0:
                continue
            ans += t - mid

        if ans < M:
            hi = mid - 1
        else:
            lo = mid + 1
    
    print(hi)





if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    tree = list(map(int, input().split()))
    solution(N,M,tree)