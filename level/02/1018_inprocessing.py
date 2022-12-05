import sys

def solution(M, N, board):
    print(board)





if __name__ == "__main__" :
    input = sys.stdin.readline
    M, N = map(int, input().split())
    board = [list(str(input().strip())) for _ in range(M)]
    solution(M, N, board)