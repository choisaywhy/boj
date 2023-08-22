import sys
def solution():
    n,m = map(int, input().split())
    board = [list(map(int,input().strip())) for _ in range(n)]
    ans = 0
    for x in range(1,n):
        for y in range(1,m):
            if board[x][y] > 0:
                board[x][y] += min(board[x-1][y-1], board[x-1][y], board[x][y-1])
    
    for x in range(n):
        for y in range(m):
            if ans >= board[x][y]:
                continue
            ans = board[x][y]


    print(ans**2)

if __name__ == "__main__" :
    input = sys.stdin.readline

    solution()



# import sys
# def solution():
#     n,m = map(int, input().split())
#     board = [list(map(int,input().strip())) for _ in range(n)]
#     ans = 0
#     for x in range(1,n):
#         for y in range(1,m):
#             if board[x][y] > 0:
#                 board[x][y] += min(board[x-1][y-1], board[x-1][y], board[x][y-1])
#             if ans < board[x][y]:
#                 ans = board[x][y]
    
#     print(ans**2)

# if __name__ == "__main__" :
#     input = sys.stdin.readline

#     solution()
