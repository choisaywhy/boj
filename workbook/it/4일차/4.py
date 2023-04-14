import sys

def solution(N, M, linked):
    parents = [ i for i in range(N+1)]

    def find(u):
        if parents[u] != u:
            parents[u] = find(parents[u])
        return parents[u]

    def union(u,v):
        pu, pv = find(u), find(v)
        parents[max(pu,pv)] = min(pu,pv)

    
    def dfs(idx, depth,temp):
        if depth == 2:
            for j in range(M):

        for i in range(idx,N):
            dfs(i+1,depth+1,temp+[i])

            
    if M < N -2:
        print(-1)
    else:
        dfs(0,0,[])
        

    





if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    linked = [tuple(map(int, input().split())) for _ in range(M)]
    solution(N, M, linked)