# 다음 턴으로 넘어갈 때 visited = False 로 변환하는 부분에서 막힘
# 백조의 호수 코드나 풀이를 다시 살펴보면 좋을 듯 함

import sys

def solution() :
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    def DFS(x, y, countY, depth) :
        nonlocal count
        print(x,y,seats[x][y],depth,'turn')

        # 백트래킹 부분 또한 손봐야함
        if countY >= 4 :
            print('Y is already full')
            return 

        if depth == 7 :
            print('===============depth completed')
            count += 1
            print(count,'<-- count')
            return

        for dx, dy in directions :
            nx, ny = dx + x, dy + y
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] :
                visited[nx][ny] = True
                print(nx,ny,'visting available')
                if seats[nx][ny] == "S" :
                    DFS(nx, ny, countY, depth+1)
                else :
                    DFS(nx, ny, countY+1, depth+1)
                visited[nx][ny] = False


    seats = []
    party = []
    for x in range(5) :
        seats.append(list(str(input().strip())))

        for y in range(5) :
            if seats[x][y] == "S" :
                party.append((x,y))
    
    if len(party) < 4:
        print(0)
        return

    visited = [[False]*5 for _ in range(5)]
    count = 0
    for p in party :
        px, py = p
        visited[px][py] = True # px, py 를 지나는 모든 행선을 파악했으므로, 더이상 탐색 안함
        DFS(px, py, 0, 1)
    print(count)



if __name__ == "__main__" :
    input = sys.stdin.readline
    solution()