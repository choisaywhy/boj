# pypy에서만 통과
import sys

def solution():
    r1, c1, r2, c2 = map(int, input().split())
    
    dx = {i : i - r1 for i in range(r1, r2+1)}
    dy = {i : i - c1 for i in range(c1, c2+1)}
    n = abs(r1)+abs(r2)+1 if r1*r2 < 0 else abs(r1-r2)+1
    m = abs(c1)+abs(c2)+1 if c1*c2 < 0 else abs(c1-c2)+1

    board = [[0]*m for _ in range(n)]

    directions = [(0,1),(-1,0),(0,-1),(1,0)] # 반시계 -> 부터
    

    direct = 0
    num = 1
    x, y = 0,0
    count = 0

    while count < n*m:
        if ((x>=0 and y>=0) and y - x == 1) or (not ( x>=0 and y>=0) and abs(x) == abs(y)):
            direct = (direct+1) % 4
        
        if r1 <= x <= r2 and c1 <= y <= c2:
            board[dx[x]][dy[y]] = num
            count += 1

        num += 1
        x, y = x + directions[direct][0], y + directions[direct][1]

    blank = len(str(num-1))

    for i in range(n):
        for j in board[i]:
            print("%*d" %(blank, j), end=" ")
        print()  

if __name__ == "__main__" :
    input = sys.stdin.readline
    solution()
