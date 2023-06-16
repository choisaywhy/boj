import sys

def solution(n,f):
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if f[i][j] <= f[i][k] + f[k][j]:
                    continue
                f[i][j] = f[i][k] + f[k][j]

    candidates = []
    score = 1e9
    for i in range(1,n+1):
        s = max(f[i][1:])
        if s < score:
            candidates = [i]
            score = s
        elif s == score:
            candidates.append(i)
    
    candidates.sort()
    print(score, len(candidates))
    print(" ".join(map(str,sorted(candidates))))



if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    f = [[1e9]*(n+1) for _ in range(n+1)]
    while True:
        a,b = map(int,input().split())
        if (a,b) == (-1,-1):
            break
        f[a][b] = min(f[a][b], 1)
        f[b][a] = min(f[b][a], 1)
    for i in range(1,n+1):
        f[i][i] = 0
    solution(n,f)