import sys
from collections import defaultdict
def solution(N, M, linked):

    def find(parents,u):
        if parents[u] != u:
            parents[u] = find(parents, parents[u])
        return parents[u]

    def union(parents,u,v):
        pu, pv = find(parents, u), find(parents, v)
        parents[max(pu,pv)] = min(pu,pv)
        return parents

    def dfs():
        stack = [(0, [])]

        while stack:
            idx, temp = stack.pop()

            if len(temp) == 2:
                parents = [ i for i in range(N+1)]
                for i in range(M):
                    if i in temp:
                        continue
                    u,v = linked[i]
                    if find(parents,u) == find(parents,v):
                        continue
                    parents = union(parents,u,v)
                if list(set(parents))[1] == list(set(parents))[2]:
                    continue
                if len(set(parents)) == 3:
                    return (temp, parents) # 삭제된 간선, 부모 관계
                continue
                

            for i in range(idx,N):
                stack.append((i+1, temp+[i]))
        return []
    


    if M < N - 2:
        print(-1)
    else:
        temp, parents = dfs()
        trees = defaultdict(list)

        a = list(set(parents))[1]
        b = list(set(parents))[2]

        for i in range(M):
            if i in temp:
                continue
            u,v = linked[i]
            trees[parents[u]].append(i)

        print(parents.count(a), parents.count(b))

        for i in range(1,N+1):
            if parents[i] == a:
                print(i,end=" ")
        print()
        print(" ".join(map(str, trees[a])))

        
        for i in range(1,N+1):
            if parents[i] == b:
                print(i,end=" ")    
        print()
        print(" ".join(map(str, trees[b])))
        

   

    





if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    linked = [tuple(map(int, input().split())) for _ in range(M)]
    solution(N, M, linked)



    # def dfs(idx, depth,temp):
    #     if depth == 2:
    #         for j in range(M):
    #             if j in temp:
    #                 continue
    #             u,v = linked[j]
    #             if find(u) == find(v):
    #                 continue
                


    #     for i in range(idx,N):
    #         dfs(i+1,depth+1,temp+[i])
