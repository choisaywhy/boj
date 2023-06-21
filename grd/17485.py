import sys

def solution(n,m,space):
    dx = [1,1,1]
    dy = [-1,0,1]
    dp = [[[1e7,1e7,1e7] for _ in range(m)] for _ in range(n)]

    for i in range(m):
        for j in range(3):
            dp[0][i][j] = space[0][i]
    
    for i in range(1, n):
        for j in range(m):
            for k in range(3):
                for l in range(3):
                    if k == l or not( 0 <= i - dx[l] < n and 0 <= j - dy[l] < m ):
                        continue
                    dp[i][j][k] = min(dp[i-dx[l]][j-dy[l]][l] + space[i][j], dp[i][j][k])

    ans = []
    for a in dp[-1]:
        ans.append(min(a))
    
    print(min(ans))



if __name__ == "__main__" :
    input = sys.stdin.readline
    n,m = map(int,input().split())
    space = [list(map(int,input().split())) for _ in range(n)]
    solution(n,m,space)