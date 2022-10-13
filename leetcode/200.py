class Solution:
    def bfs(self, grid, v) :
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        queue = collections.deque([v])
        visited = [v]

        while queue :
            nx,ny = queue.popleft()
            grid[nx][ny] = "0"
            for x, y in directions :
                if (0 <= nx + x < len(grid)) and (0 <= ny + y < len(grid[0])) :
                    if grid[nx+x][ny+y] == "1" and (nx+x, ny+y) not in  visited:
                        visited.append((nx+x, ny+y))
                        queue.append((nx+x, ny+y))

        return grid
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        for x in range(len(grid)) :
            for y in range(len(grid[0])) :
                if grid[x][y] == "0" :
                    continue
                grid = self.bfs(grid, (x,y))
                count += 1
        
        return count
    