import sys
from copy import deepcopy

def solution(n,m,board):

    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    def check_cross(board,x,y,length):
        board[x][y] = "*"
        for dx, dy in directions:
            for i in range(1, length+1):
                nx, ny = x + dx * i, y + dy * i
                board[nx][ny] = "*"
        return board

    def dfs(depth, score, board):
        nonlocal ans

        if depth == 2:
            width = (1+ 4*score[0]) * (1+ 4*score[1])
            if width > ans:
                ans = width
            return
        

        for x in range(n):
            for y in range(m):
                if board[x][y] != "#":
                    continue
                length = []

                for dx, dy in directions: # 상하좌우
                    tmp = 0

                    for i in range(1,8):
                        nx, ny = x + dx * i, y + dy * i
                        if not (0 <= nx < n and 0 <= ny < m) or board[nx][ny] != '#':
                            break
                        tmp = i
                    length.append(tmp) # 각 상하좌우의 최대 길이

                for i in range(min(length)+1):
                    if ans // (1+i*4) > (min(n,m) // 2 * 4) + 1: # 격자판 내의 최대 크기와 현재 i 길이 십자가를 조합해도 ans를 넘기지 못하는 경우
                        continue
                    score.append(i)
                    dfs(depth+1, score, check_cross(deepcopy(board), x,y,i))
                    score.pop()
    ans = 0

    dfs(0,[],board)
    print(ans)


if __name__ == "__main__" :
    input = sys.stdin.readline
    n,m = map(int,input().split())
    board = [list(map(str, input().strip())) for _ in range(n)]
    solution(n,m,board)

    