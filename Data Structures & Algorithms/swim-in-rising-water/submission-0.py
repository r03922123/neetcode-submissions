class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # 1. greedily visit neighbor of small number, cache the neighbor with max number
        #     eloge, e = n*n * 4, 
        #     4 * n*n * 2 log 2*n
        # 2. binary search + bfs
        #     n*n * 2 * log(n)
        m, n = len(grid), len(grid[0])
        dirs = [-1, 0, 1, 0, -1]
        pq = [(grid[0][0], 0, 0)]
        res = 0
        while pq:
            v, i, j = heapq.heappop(pq)
            res = max(res, v)
            if i == m - 1 and j == n - 1: return res
            grid[i][j] = -1
            
            for k in range(4):
                dx, dy = dirs[k], dirs[k + 1]
                x, y = i + dx, j + dy
                if m > x >= 0 <= y < n and grid[x][y] > -1:
                    heapq.heappush(pq, (grid[x][y], x, y))
        