import sys

def solution(n,m,cost,routes):
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if cost[i][j] <= cost[i][k] + cost[k][j]:
                    continue

                cost[i][j] = cost[i][k] + cost[k][j]
                routes[i][j] = routes[i][k]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if cost[i][j] == 1e9:
                print("0", end=" ")
            else:
                print(cost[i][j], end=" ")
        print()


    for i in range(1,n+1):
        for j in range(1,n+1):
            if routes[i][j] == 0 or routes[i][j] == 1e9:
                print("0")
                continue
            nxt = i
            route = [i]
            while True:
                if routes[nxt][j] == j:
                    break
                nxt=routes[nxt][j]
                route.append(nxt)
            route.append(j)
            print(len(route), " ".join(map(str, route)))



if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    cost = [[1e9]*(n+1) for _ in range(n+1)]
    routes = [[0]*(n+1) for _ in range(n+1)]

    
    for _ in range(m):
        a,b,c = map(int, input().split())
        if cost[a][b] <= c:
            continue
        cost[a][b] = min(c, cost[a][b])
        routes[a][b] = b

    for i in range(1,n+1):
        cost[i][i] = 0
    
    solution(n,m,cost,routes)