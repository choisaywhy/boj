# 뿌요 방문 파악 시, 길이가 아닌 좌표로 파악해야 함. ex> 8개 뿌요 중, 4개 같은곳 방문 후 4개 같은 곳 방문
import sys
from collections import deque

def solution(maps, puyo):
    def BFS(sx,sy,color):
        direc = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque([(sx,sy)])
        linked = [(sx,sy)]

        while queue :
            nx, ny = queue.popleft()
            for d in direc:
                x, y = d[0] + nx, d[1] + ny
                if 0 <= x < 12 and 0 <= y < 6 and maps[x][y] == color and (x,y) not in linked:
                    linked.append((x,y))
                    queue.append((x,y))
        if len(linked) >= 4: # 연결 뿌요가 4개 이상이면
            for l in linked :
                maps[l[0]][l[1]] = "." # 터트리기
        
        return linked # 방문한 뿌요 좌표 retrun

    days = 0
    while True :
        flag = False # 터트린 뿌요 있는지 확인할 flag
        for color, locate in puyo.items() : # 색깔별로 뿌요 좌표 iter
            if len(locate) < 4 : # 4개 이상 뿌요가 없으면 무시
                continue
            visited = [] # 확인한 뿌요 개수 파악
            for index in locate :
                ix,iy = index 
                if (ix,iy) in visited :
                    continue
                linked = BFS(ix,iy,color) # 뿌요 터트림 확인
                if len(linked) >= 4 : # 뿌요 4개 이상이면, 연쇄 확인
                    flag = True 
                visited.extend(linked) # 방문한 노드 개수 업데이트
        
        if not flag : # 연쇄 실패시
            break # while문 나가기
        
        # 연쇄 성공시, maps 갱신
        puyo = {"R":[], "G":[], "B":[], "P":[], "Y":[]} # 다음 터트릴 뿌요 갱신
        for y in range(6) :
            num = 0 # 삭제된 뿌요 개수
            for x in range(11,-1,-1) : # 아래서 부터 iter
                if maps[x][y] == "." :
                    num += 1
                    continue
                if num : # 내려가야할 뿌요가 있으면
                    maps[x+num][y] = maps[x][y]
                    maps[x][y] = "."
                puyo[maps[x+num][y]].append((x+num, y)) # 다음 터트릴 뿌요에 갱신

        days += 1 # 연쇄 숫자 업데이트

    print(days)

if __name__ == "__main__" :
    input = sys.stdin.readline

    maps = []
    puyo = {"R":[], "G":[], "B":[], "P":[], "Y":[]} # 연쇄 파악할 좌표를 color 별로 저장
    for x in range(12):
        maps.append(list(str(input().strip())))
        for y in range(6):
            if maps[x][y] == "." :
                continue
            puyo[maps[x][y]].append((x,y))

    solution(maps, puyo)
