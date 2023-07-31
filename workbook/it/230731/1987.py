import sys
def solution():
    r,c = map(int,input().split())
    board = [list(map(lambda x : ord(x) - ord("A"), input().strip())) for _ in range(r)]
    alphabet = [False]*(26)
    ans = 0

    def dfs(x,y,depth):
        nonlocal ans

        for d in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx, ny = d[0]+x, d[1]+y
            if not(0<=nx<r and 0<=ny<c) or alphabet[board[nx][ny]]:
                continue
                
            alphabet[board[nx][ny]] = True
            dfs(nx,ny,depth+1)
            alphabet[board[nx][ny]] = False


        if depth > ans:
            ans = depth
    
    alphabet[board[0][0]] = True
    dfs(0,0,1)
    print(ans)

            
if __name__ == "__main__" :
    input = sys.stdin.readline

    solution()