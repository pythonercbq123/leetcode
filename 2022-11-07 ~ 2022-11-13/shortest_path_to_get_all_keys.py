from typing import List
from collections import deque


class Solution:
    def bfs(self, grid: List):
        if not grid:
            return -1
        # find the start
        rows = len(grid)
        cols = len(grid[0])
        sx = sy = 0
        key_to_idx = {}
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '@':
                    sx, sy = (i, j)
                elif grid[i][j].islower():
                    if grid[i][j] not in key_to_idx:
                        idx = len(key_to_idx)
                        key_to_idx[grid[i][j]] = idx

        queue = deque()
        queue.append((sx, sy, 0))
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        dist = dict()
        dist[(sx, sy, 0)] = 0
        while queue:
            x, y, mask = queue.popleft()
            for dx, dy in dirs:
                nx = dx + x
                ny = dy + y
                if 0 <= nx < rows and 0 <= ny < cols and grid[x][y] != '#':
                    if grid[nx][ny] == '.' or grid[nx][ny] == '@':
                        dist[(nx, ny, mask)] = dist[(x, y, mask)] + 1
                        queue.append((nx, ny, mask))
                    elif grid[nx][ny].islower():
                        idx = key_to_idx[grid[nx][ny]]
                        if (nx, ny, mask | 1 << idx) not in dist:
                            dist[(nx, ny, mask | 1 << idx)] = dist[(x, y, mask)] + 1
                            if (mask | 1 << idx) == (1 << len(key_to_idx)) - 1:
                                return dist[(nx, ny, mask | 1 << idx)]
                            queue.append((nx, ny, mask | 1 << idx))
                    else:
                        idx = key_to_idx[grid[nx][ny]]
                        if mask & (1 << idx) and (nx, ny, mask) not in dist:
                            dist[(nx, ny, mask)] = dist[(x, y, mask)] + 1
                            queue.append((nx, ny, mask))

        return -1




