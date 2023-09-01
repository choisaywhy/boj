import sys
def solution(board):
    board = list(board)
    tictacttoe = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ] # 가로 세로 대각선 경우의 수
    o = board.count('O')
    x = board.count('X')
    flag = True
    ttt = "."

    # o과 x 개수 차이가 1 초과 나는 경우 (순서를 안지킨 경우)
    if not ( o == x or o + 1 == x):
        flag = False

    # 틱택토 연산
    for i,j,k in tictacttoe:
        if not(board[i] == board[j] == board[k] != "."):
            continue
        if ttt not in ['.',board[i]]: # 서로다른 틱택토가 두개 이상 존재할 경우
            flag = False
            break
        ttt = board[i]
    
    # 틱택토가 있을 때
    if ttt != '.':
        if o == x: # o가 이기고 끝난 경우
            if ttt != 'O':
                flag = False
        elif o + 1 == x: # x가 이기고 끝난 경우
            if ttt != 'X':
                flag = False

    # 틱택토가 없을 때
    else:
        if '.' in set(board): # 빈칸 있게 끝난 경우
            flag= False
    


    if flag:
        print("valid")
    else:
        print("invalid")





if __name__ == "__main__" :
    input = sys.stdin.readline
    while True:
        board = str(input().strip())
        if board == "end":
            break
        solution(board)
