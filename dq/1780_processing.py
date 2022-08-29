import sys
from collections import deque

input = sys.stdin.readline

def check(node,paper,cutter,answer={-1:0,0:0,1:0}) :
    nx,ny = node
    piece = paper[nx][ny:ny+cutter]
    for x in range(cutter) :
        for y in range(cutter):
            if piece != paper[nx+x][ny+y:ny+y+cutter] :
                answer = check(node,paper,cutter//3,answer)
            


            


N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

length = N

print(check((0,0),paper,length))