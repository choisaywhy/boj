import sys
from collections import deque

input = sys.stdin.readline

def DFS(target, cave):
    pass



R, C = map(int, input().split())
cave = []

for x in range(R) :
    cave.append(list(map(str, input().strip())))

N = int(input())
height = list(map(int, input().split()))
turn = True

for H in height :
    x = R-H
    if turn : # 왼쪽에서 오른쪽
        y = cave[x].find('x')
    else :
        y = cave[x][::-1].find('x')
    if y == -1 :
        continue
    cave[x][y] = '.'
    DFS((x,y), cave)


    turn = not turn

