import sys
from collections import deque

def solution(n,m,paper) :
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    def BFS(sx,sy) :
        queue = deque([(sx,sy)])
        width = 1

        while queue :
            nx, ny = queue.popleft()
            for dx, dy in directions :
                x, y = nx + dx, ny + dy
                if 0 <= x < n and 0 <= y < m and paper[x][y] == 1: # visited 확인 후
                    paper[x][y] = 0 # 바로 visited true 해주면 반복 될 일이 전혀 없다 이말임
                    width += 1
                    queue.append((x,y))

        return width

    count = 0 
    max_depth = 0
    for sx in range(n) :
        for sy in range(m) :
            if paper[sx][sy] == 0 :
                continue
            paper[sx][sy] = 0
            max_depth = max(BFS(sx,sy), max_depth)
            count += 1
            print(max_depth)
            for i in range(n) :
                print(paper[i])

    print(count, max_depth)




if __name__ == "__main__" :
    input = sys.stdin.readline
    n, m = map(int, input().split())
    paper = [list(map(int, input().split())) for _ in range(n)]

    solution(n,m,paper)