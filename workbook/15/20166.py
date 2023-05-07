import sys

def solution(N, M, K, board, keywords):
    ans = {}
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    def dfs(x,y,keyword):
        stack = [(x,y,0)]
        count = 0

        while stack :
            x, y, depth = stack.pop()
            if depth == len(keyword)-1:
                count += 1
                continue
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                if not (0<=nx<N):
                    if nx < 0:
                        nx = N-1
                    else:
                        nx = 0
                if not (0<=ny<M):
                    if ny < 0:
                        ny = M-1
                    else:
                        ny = 0
                if board[nx][ny] != keyword[depth+1]:
                    continue
                stack.append((nx,ny,depth+1))
        return count    

        
    
    for keyword in keywords:
        if ans.get(keyword, False):
            print(ans[keyword])
            continue
        count = 0
        for x in range(N):
            for y in range(M):
                if board[x][y] == keyword[0]:
                    count += dfs(x,y,keyword)

        print(count)
        ans[keyword] = count





if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M, K = map(int,input().split())
    board = [list(map(str, input().strip())) for _ in range(N)]
    keywords = [input().strip() for _ in range(K)]
    solution(N, M, K, board, keywords)