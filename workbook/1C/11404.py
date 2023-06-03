# 3중 for문으로 무거우므로, 연산을 조금더 단순화 하는 것이 시간에 좋음
import sys

def solution(n,m,cost):

    # for k in range(1,n+1):
    #     for i in range(1,n+1):
    #         for j in range(1,n+1):
    #             cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if cost[i][j] <= cost[i][k]+cost[k][j]:
                    continue
                cost[i][j] = cost[i][k]+cost[k][j]

                
    for i in range(1,n+1):
        for j in range(1,n+1):
            if cost[i][j] == 1e9:
                print("0", end=" ")
            else:
                print(cost[i][j], end=" ")
        print()



if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    cost = [[1e9]*(n+1) for _ in range(n+1)]

    
    for _ in range(m):
        a,b,c = map(int, input().split())
        cost[a][b] = min(c, cost[a][b])
    for i in range(1,n+1):
        cost[i][i] = 0
    
    solution(n,m,cost)