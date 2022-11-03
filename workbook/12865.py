import sys

input = sys.stdin.readline

N, K = map(int, input().split())
bag = [[0]* (K+1) for _ in range(N+1)] 

for i in range(1,N+1):
    W, V = map(int, input().split())

    for j in range(1,K+1) :
        if W > j :
            bag[i][j] = bag[i-1][j]
        else :
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-W]+V)
print(bag[N][K])