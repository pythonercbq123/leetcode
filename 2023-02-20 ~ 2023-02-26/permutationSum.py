from typing import List
from collections import deque


class Solution:
    def max_area(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0] * cols for _ in range(rows)]
        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and not visited[row][col]:
                    area = self.get_max_area(visited, grid, row, col)
                    max_area = max(area, max_area)
        return max_area

    def get_max_area(self, visited, grid, row, col):
        q = deque()
        q.append((row, col))
        visited[row][col] = 1
        dxy = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        area = 0
        while q:
            r, c = q.popleft()
            area += 1
            for dx, dy in dxy:
                x = r + dx
                y = c + dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and visited[x][y] == 0:
                    q.append((x, y))
                    visited[x][y] = 1
        return area


if __name__ == '__main__':
    s = Solution()
    ret = s.max_area([[1, 1, 0, 0, 1], [1, 0, 0, 1, 0], [1, 1, 0, 1, 0], [0, 0, 1, 0, 0]])
    print(ret)
