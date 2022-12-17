import sys
from collections import deque

def solution(maps, puyo):
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    def boom(sx,sy,color) :
        stack = deque((sx,sy))
        linked = [(sx,sy)]

        while stack :
            x,y = stack.popleft()
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < 12 and 0 <= ny < 6 and maps[nx][ny] == color and (nx,ny) not in linked:
                    stack.append((nx,ny))
                    linked.append((nx,ny))

        if len(linked) >= 4 :
            puyo[color] = list(set(puyo[color]) - set(linked))
            return linked, True
        return linked, False

    def relocate(maps):
        pass


    count = 0
    while True :
        flag = False
        visitedy = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]} # 터질 애들
        for color, locate in puyo :
            total = len(locate)
            for l in locate :
                lx,ly = l
                if total - visitedy[color] < 4 :
                    continue
                if lx not in visitedy[ly] :
                    if boom(lx,ly,color) :
                        flag = True
        for v in visitedy :
            vx, vy = v
            maps[vx][vy] = "."
        
            
        if not flag :
            break
    print(count)
        






if __name__ == "__main__" :
    input = sys.stdin.readline

    maps = []
    puyo = {"R":[], "G":[], "B":[], "P":[], "Y":[]}
    for x in range(12):
        maps[x] = list(map(str, input().strip().split()))
        for y in range(6):
            if maps[x][y] == "." :
                continue
            puyo[maps[x][y]].append((x,y))

    solution(maps, puyo)