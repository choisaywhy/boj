import sys
from heapq import *
def solution(n,m,maze):
    
    cost = [[1e5]*m for _ in range(n)]
    cost[0][0] = 0
    queue = [(cost[0][0],(0,0))]

    while queue:
        walls, node = heappop(queue)
        x,y = node
        if cost[x][y] < walls:
            continue

        for nx, ny in [(1,0),(-1,0),(0,1),(0,-1)]:
            dx, dy = nx+x, ny+y
            if not(0 <= dx < n and 0 <= dy < m) or cost[dx][dy] <= walls + int(maze[dx][dy]):
                continue
            
            cost[dx][dy] = walls + int(maze[dx][dy])
            heappush(queue, (cost[dx][dy], (dx,dy)))
    
    print(cost[-1][-1])
        




if __name__ == "__main__" :
    input = sys.stdin.readline
    m,n = map(int, input().split())
    maze = [list(input().strip()) for _ in range(n)]
    solution(n,m,maze)