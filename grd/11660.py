# https://www.acmicpc.net/source/63951217 참고

import sys

def solution():
    n,m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    row = [[0]*n for _ in range(n)]
    column = [[0]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if x != 0:
                column[x][y] = board[x][y] + column[x-1][y]
            else:
                column[x][y] = board[x][y]
            if y != 0:
                row[x][y] = board[x][y] + row[x][y-1]
            else:
                row[x][y] = board[x][y]

    for _ in range(m):
        x1,y1,x2,y2 = map(int,input().split())
        x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1 
        if (x1,y1) == (x2,y2):
            print(board[x1][y1])
            continue
        if x1 < y1:
            if x1 == 0:
                print(sum(list(column[x][y2] for x in range(x1, x2+1))))
            else:
                print(sum(list(column[x][y2] for x in range(x1, x2+1)))-sum(list(column[x][y1-1] for x in range(x1,x2+1))))
        else: # x1 >= y1
            if y1 == 0:
               print(sum(list(row[x][y2] for x in range(x1, x2+1))))
            else:
                print(sum(list(row[x][y2] for x in range(x1, x2+1)))-sum(list(row[x][y1-1] for x in range(x1,x2+1)))) 



if __name__ == "__main__" :
    input = sys.stdin.readline
    

    solution()





# 문제 이해 오류 x1,y1 x2,y2 두 꼭짓점을 가지는 사각형의 누적합을 구해야함
# import sys

# def solution():
#     n,m = map(int,input().split())
#     board = [[0]*(n+1)] + [[0]+list(map(int,input().split())) for _ in range(n)]

#     for x in range(1,n+1):
#         if x != 1:
#             board[x][0] = board[x-1][-1]
#         for y in range(1,n+1):
#             board[x][y] += board[x][y-1]

#     print(board)
#     for _ in range(m):
#         x1,y1,x2,y2 = map(int,input().split())

#         if (x1,y1) == (x2,y2):
#             print(board[x1][y1] - board[x1][y1-1])
#         elif (min(x1,x2), min(y1,y2)) == (1,1):
#             print(board[max(x1,x2)][max(y1,y2)])
#         else:
#             print(board[max(x1,x2)][max(y1,y2)] - board[min(x1,x2)][min(y1,y2)])


# if __name__ == "__main__" :
#     input = sys.stdin.readline
    

#     solution()


# import sys

# def solution():
#     n,m = map(int,input().split())
    # board = [[0]*(n+1)] + [[0]+list(map(int,input().split())) for _ in range(n)]

    # for x in range(1,n+1):
    #     if x != 1:
    #         board[x][0] = board[x-1][-1]
    #     for y in range(1,n+1):
    #         board[x][y] += board[x][y-1]

#     print(board)
#     for _ in range(m):
#         x1,y1,x2,y2 = map(int,input().split())

#         if (x1,y1) == (1,1) or (x1,y1) == (x2,y2):
#             print(board[x2][y2] - board[x1][y1-1])
#             print('irregular')
#         else:
#             print(board[x2][y2] - board[x1][y1])



# if __name__ == "__main__" :
#     input = sys.stdin.readline
    

#     solution()
