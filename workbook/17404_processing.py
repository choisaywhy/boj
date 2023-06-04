import sys

def solution(N, color):

    for j in range(1,N) :
        color[j][0] = color[j][0] + min(color[j-1][1], color[j-1][2])
        color[j][1] = color[j][1] + min(color[j-1][0], color[j-1][2])
        color[j][2] = color[j][2] + min(color[j-1][0], color[j-1][1])
    
    print(min(color[-1]))





if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    color = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(3):
            color[i][j] = (color[i][j], j)
    solution(N, color)