import sys

def solution(m,n,roads,cost):
    parents = [i for i in range(m)]
    roads.sort()

    def find(x) :
        if parents[x] != x :
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(x, y) :
        px, py = find(x), find(y)
        parents[max(px, py)] = min(px, py)
    
    for i in range(n) :
        z, x, y = roads[i]

        if find(x) == find(y) :
            continue
        union(x,y)
        cost -= z
    
    print(cost)





if __name__ == "__main__" :
    input = sys.stdin.readline
    while True :
        m, n = map(int, input().split())
        if (m,n) == (0,0) :
            break
        cost = 0
        roads = []
        for _ in range(n) :
            x, y, z = map(int, input().split())
            roads.append((z,x,y))
            cost += z

        solution(m,n,roads,cost)