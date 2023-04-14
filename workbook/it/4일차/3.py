import sys
from collections import deque
def solution(N, cave):
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    def bfs():
        dp = [[1e9]*N for _ in range(N)]
        queue = deque([(0,0)])
        dp[0][0] = cave[0][0]

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not ( 0 <= nx < N and 0 <= ny < N):
                    continue
                if dp[nx][ny] <=  dp[x][y] + cave[nx][ny]:
                    continue
                dp[nx][ny] =  dp[x][y] + cave[nx][ny]
                queue.append((nx,ny))
        
        return dp[-1][-1]

    return bfs()



if __name__ == "__main__" :
    input = sys.stdin.readline
    problem = 1
    while True:
        N = int(input())
        if N == 0:
            break
        cave = [list(map(int, input().split())) for _ in range(N)]

        print("Problem ", problem,": ",solution(N, cave),sep="")
        problem += 1