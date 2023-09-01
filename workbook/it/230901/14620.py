import sys
def solution():
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    ans = 1e6

    def dfs(cost, depth):
        nonlocal ans, visited
        if depth == 3:
            if ans > cost:
                ans = cost
            return
        else:  
            if ans < cost:
                return
        
        for x in range(1,n-1):
            for y in range(1,n-1):
                if visited[x][y]:
                    continue
                flag = True
                
                for i in range(4):
                    nx,ny = x+ dx[i], y +dy[i]
                    if not( 0<= nx < n or 0 <= ny < n) or visited[nx][ny]:
                        flag = False
                        break
                if not flag:
                    continue
                
                tmp = board[x][y]
                visited[x][y] = True
                for i in range(4):
                    nx,ny = x+ dx[i], y +dy[i]
                    visited[nx][ny] = True
                    tmp += board[nx][ny]
                
                dfs(cost+tmp, depth+1)
                visited[x][y] = False
                for i in range(4):
                    nx,ny = x+ dx[i], y +dy[i]
                    visited[nx][ny] = False

                

    dfs(0,0)
    print(ans)

    
            

if __name__ == "__main__" :
    input = sys.stdin.readline


    solution()
