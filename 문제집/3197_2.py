import sys
from collections import deque

input = sys.stdin.readline
directions = [(1,0), (-1,0), (0,1), (0,-1)]

def lakeBFS(nextLake, visitedLake, lake) :
    
    while nextLake :
        x, y = nextLake.popleft()
        lake[x][y]




def swanBFS(nextSwan, visitedSwan, destination, lake):
    pass


R, C = map(int, input().split())
lake = []
destination = ()
nextLake = deque([])
nextSwan = deque([])
visitedLake = [[False]*C for _ in range(R)]
visitedSwan = [[False]*C for _ in range(R)]

for x in range(R) :
    lake.append(list(map(str, input().strip())))
    for y in range(C) :
        if lake[x][y] == 'L' :
            if not destination :
                destination = (x,y)
            else :
                nextSwan.append((x,y))
                visitedSwan[x][y] = True
            lake[x][y] = '.'

        if lake[x][y] == '.' :
            nextLake.append((x,y))
            visitedLake[x][y] = True

day = 0
while True :
    day += 1
    nextLake, visitedLake, lake = lakeBFS(nextLake, visitedLake, lake)
    nextSwan, visitedSwan, flag = swanBFS(nextSwan, visitedSwan, destination, lake)
    if flag :
        print(day)
        break