from typing import List


class Solution:
    DIRS = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(row, col):
            if memo[row][col] != 0:
                return memo[row][col]
            memo[row][col] += 1
            for dx, dy in Solution.DIRS:
                new_row, new_col = dx + row, dy + col
                if 0 <= new_row < m and 0 <= new_col < n and matrix[new_row][new_col] > matrix[row][col]:
                    memo[row][col] = max(memo[row][col], dfs(new_row, new_col) + 1)
            return memo[row][col]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans