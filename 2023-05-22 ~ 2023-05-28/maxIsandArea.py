class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    max_area = max(max_area, self.dfs(grid, i, j))
        return max_area

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        return 1 + self.dfs(grid, i - 1, j) + \
            self.dfs(grid, i + 1, j) + \
            self.dfs(grid, i, j - 1) + \
            self.dfs(grid, i, j + 1)
