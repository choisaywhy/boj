import sys
from collections import deque

def solution(N, M, board):

    res = []
    for i in range(N-7) :
        for j in range(M-7) :
            sw, sb = 0, 0
            for x in range(i, i+8):
                for y in range(j,j+8):
                    if (x + y) % 2 == 0 :
                        if board[x][y] != 'W' :
                            sw += 1
                        else :
                            sb += 1
                    else :
                        if board[x][y] != 'W' :
                            sb += 1
                        else :
                            sw += 1
            res.extend([sw,sb])
    print(min(res))


    

if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [list(str(input().strip())) for _ in range(N)]
    solution(N, M, board)