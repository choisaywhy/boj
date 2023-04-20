import sys

def solution(H, W, maps):
    ops = []
    face = 0
    dir = [(-1,0),(0,1),(1,0),(0,-1)] # 상우하좌 # l : (x+3)%4, r : (x+1)%4
    head = ["^", ">", "v", "<"]


    def dfs(start):
        nonlocal face
        stack = [start]

        while stack:
            x, y = stack.pop()
            for idx in range(3): # 직진, 왼쪽, 오른쪽
                move = [dir[face], dir[(face+3)%4], dir[(face+1)%4]]
                ndx, ndy = move[idx]
                dx, dy = move[idx][0]*2, move[idx][1]*2
                if not (0 <= dx + x < H and 0 <= dy + y < W) or maps[dx + x][dy + y] == "." or maps[ndx + x][ndy + y] == ".":
                    continue

                stack.append((dx+x,dy+y))
                maps[dx + x][dy + y] == "." 
                maps[ndx + x][ndy + y] == "."

                if idx == 0:
                    ops.append('A')
                elif idx == 1:
                    ops.append('LA')
                    face = (face+3)%4
                elif idx == 2:
                    ops.append('RA')
                    face = (face+1)%4
                
        print("".join(ops))



    for x in range(H):
        for y in range(W):
            if maps[x][y] == '#': 
                count = 0
                for idx in range(4):
                    dx, dy = dir[idx]
                    if not (0 <= dx + x < H and 0 <= dy + y < W) or maps[dx + x][dy + y] == ".": # x,y의 상하좌우로 연결된 #이 하나인 경우. 즉, 경로의 끝점인 경우
                        continue
                    count += 1
                    face = idx

                if count == 1:
                    print(x+1,y+1)
                    print(head[face])
                    maps[x][y] = "."
                    dfs((x,y))
                    return



if __name__ == "__main__" :
    input = sys.stdin.readline
    H,W = map(int, input().split())
    maps = [ list(map(str, input().strip())) for _ in range(H)]
            
    solution(H, W, maps)