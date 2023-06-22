# copy 이슈 해결 후, 예제 디버깅 중

import sys
import copy

def solution(f,d,o):
    directions = {1:(-1,0), 2:(-1,-1), 3:(0,-1), 4:(1,-1), 5:(1,0),
              6: (1,1), 7:(0,1), 8:(-1,1)} # (x+1) % 8 : 45 반시계 회전

    def check(fish):
        nonlocal ans
        count = 0
        for idx in range(1,17):
            if fish[idx] == []: # eaten
                count += idx
        if count > ans:
            ans = count
            
    def fish_move(ocean, fish, direct):
        for idx in range(1,17):
            if fish[idx] == []: # already eaten
                continue
            x,y = fish[idx]
            for i in range(8):
                tmp = (direct[idx]+i)%8
                if tmp == 0:
                    tmp = 8
                dx, dy = directions[tmp]
                if not ( 0 <= x+dx < 4 and 0 <= y+dy < 4) or ocean[x+dx][y+dy] == -1:
                    continue
                next = ocean[x+dx][y+dy]
                fish[idx], direct[idx] = [x+dx, y+dy], tmp
                if next != 0:
                    fish[next] = [x,y]
                ocean[x][y], ocean[x+dx][y+dy] = next, idx
                break
        return ocean[:], fish[:], direct[:]
    
    def shark_move(sx,sy,sd, ocean): # 상어가 갈 수 있는 경로 return
        routes = []
        dx, dy = directions[sd]
        while 0 <= sx + dx < 4 and 0 <= sy + dy < 4 and ocean[sx+dx][sy+dy] > 0:
            routes.append((sx+dx,sy+dy))
            sx, sy = sx + dx, sy + dy

        return routes

    
    def dfs(sx,sy,sd,ocean, fish, direct): # 상어 현재 위치, 방향
        print(sx,sy,sd,'turn')
        to, tf, td = fish_move(ocean, fish, direct)
        routes = shark_move(sx,sy,sd,to)


        if not routes:
            print("shark cant go anymore")
            print('ocean',to)
            print('sharks at',sx,sy,sd)
            check(tf)
            return
        
        print('sharks at',sx,sy,sd)
        print(routes,'routes')
        to[sx][sy] = 0
        for r in routes:
            nx,ny = r
            eaten = to[nx][ny]
            tf[eaten] = []
            to[nx][ny] = -1

            print('ocean',to)
            print('fish',tf)
            print('direct',td)
            print('eaten',eaten)
            print('nx,ny',nx,ny)
            print('sx,sy',sx,sy)

            dfs(nx,ny,td[eaten],copy.deepcopy(to),copy.deepcopy(tf),copy.deepcopy(td))
            tf[eaten] = [nx,ny]
            to[nx][ny] = eaten
        to[sx][sy] = -1

    ans = 0

    sx,sy,sd = 0,0,d[o[0][0]]
    f[o[0][0]] = []
    o[0][0] = -1

    dfs(sx,sy,sd,o, f, d)
    print(ans)

        

if __name__ == "__main__" :
    input = sys.stdin.readline
    f = [[0,0] for _ in range(17)]
    d = [0]*17
    o = [[0]*4 for _ in range(4)]
    for x in range(4):
        tmp = list(map(int,input().split()))
        for y in range(0,8,2):
            f[tmp[y]] = [x,y//2]
            d[tmp[y]] = tmp[y+1]
            o[x][y//2] = tmp[y]
    solution(f,d,o)

    