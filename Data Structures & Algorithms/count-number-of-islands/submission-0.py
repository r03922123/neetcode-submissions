class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate all point row by row, start dfs if cell '1', mask cell to '0'
        # after dfs, add global island count by 1

        def dfs(i, j, m, n, dirs):
            grid[i][j] = '0'
            for k in range(4):
                x, y = i + dirs[k], j + dirs[k + 1]

                if m > x >= 0 <= y < n and grid[x][y] == '1':
                    dfs(x, y, m, n, dirs)

        m, n = len(grid), len(grid[0])    
        island_cnt = 0
        dirs = [-1, 0, 1, 0, -1]
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == '1':
                    island_cnt += 1
                    dfs(i, j, m, n, dirs)
        
        return island_cnt