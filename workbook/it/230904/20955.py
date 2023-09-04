# 진행 중
import sys
from collections import defaultdict
def solution():
    n,m = map(int,input().split())
    neuron  = defaultdict(list)
    parents = [i for i in range(n+1)]

    def find(a,parents):
        if parents[a] != a:
            parents[a] = find(parents[a],parents)
            return parents[a]
    
    def union(a,b,parents):
        ap, bp = find(a,parents), find(b,parents)
        parents[max(ap,bp)] = min(ap,bp)
        return parents
        
        

    for _ in range(m):
        u,v = map(int,input().split())
        neuron[u].append(v)
        neuron[v].append(u)



if __name__ == "__main__" :
    input = sys.stdin.readline

    solution()
