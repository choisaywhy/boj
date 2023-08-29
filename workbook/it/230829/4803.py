import sys
def solution():
    def find(parents,a):
        if parents[a] != a:
            parents[a] = find(parents, parents[a])
        return parents[a]
    
    def union(parents,a,b):
        ap, bp = find(parents, a), find(parents,b)
        parents[max(ap,bp)] = min(ap,bp)
        return parents
    
    case = 1

    while True:
        n,m = map(int,input().split())
        if (n,m) == (0,0):
            break
        graph = [[] for _ in range(n+1)]
        visited = [False]*(n+1)
        parents = [i for i in range(n+1)]
        has_cycle = [False]*(n+1)

        for _ in range(m):
            a,b = map(int,input().split())
            graph[a].append(b)
            graph[b].append(a)
            ap,bp = find(parents,a),find(parents,b)
            if ap==bp or has_cycle[ap] or has_cycle[bp]:
                has_cycle[ap] = True
                has_cycle[bp] = True
            parents = union(parents, a,b)
        
        root = []
        for i in range(1,n+1):
            if parents[i] == i and not has_cycle[i]:
                root.append(i)

        
        trees = 0
        for r in root:
            stack = [r]
            visited[r] = True
            cycle = False

            while stack:
                node = stack.pop()
                for next in graph[node]:
                    if visited[next]:
                        continue
                    visited[next] = True
                    stack.append(next)
            if not cycle:
                trees += 1
        
        if trees == 0:
            print("Case ",case,": No trees.",sep= "")
        elif trees == 1:
            print("Case ",case,": There is one tree.",sep= "")
        else:
            print("Case ",case,": A forest of ",trees," trees.",sep= "")

        case += 1




            

        
        

        




if __name__ == "__main__" :
    input = sys.stdin.readline


    solution()
