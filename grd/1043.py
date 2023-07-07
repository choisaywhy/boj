import sys

def solution():
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x,y):
        px = find(x) 
        py = find(y)
        if truth[px]:
            parents[py] = px
        elif truth[py]:
            parents[px] = py
        else:
            parents[max(px,py)] = min(py,px)

    n,m = map(int,input().split())

    truth = [False]*(n+1)
    parents = [i for i in range(n+1)]
    ans = 0

    for t in list(map(int,input().split()))[1:]:
        truth[t] = True
    parties = [list(map(int,input().split())) for _ in range(m)]
    for party in parties:
        party = party[1:]
        x = party[0]
        for y in party[1:]:
            if find(x) == find(y):
                continue
            union(x,y)
    for party in parties:
        if truth[find(party[1])]:
            continue
        ans += 1

    print(ans)





if __name__ == "__main__" :
    input = sys.stdin.readline

    solution()
