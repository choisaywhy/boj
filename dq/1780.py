import sys
from collections import deque

input = sys.stdin.readline

def dq(paper, node, cutter) :
    global answer
    x,y = node
    for cx in range(cutter):
        for cy in range(cutter):
            if paper[x][y] != paper[cx+x][cy+y]:
                for nx in range(3):
                    for ny in range(3):
                        dq(paper, (x + (nx * cutter // 3), y + (ny * cutter // 3)), cutter//3)
                return 

    answer[paper[x][y]] += 1
    return 


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
answer = {-1:0,0:0,1:0}

dq(paper,(0,0),N)
for _ in range(-1,2):
    print(answer[_])


