import sys
from collections import defaultdict

def solution(n,a):
    a = sorted(list(set(a)), reverse=True) # 중복제거, 길이가 긴 순서대로
    prefix = defaultdict(list)
    n = len(a)

    for i in range(n-1):
        for j in range(i+1,n):
            if a[j] != a[i][:len(a[j])]:
                continue
            prefix[a[j]].append(a[i])

    print(len(a) - len(prefix))





if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    a = [input().strip() for _ in range(n)]
    solution(n,a)

    