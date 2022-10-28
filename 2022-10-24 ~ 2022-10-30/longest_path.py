from typing import List


class Solution:
    def longest_path(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        longest = 0
        for i in range(m):
            for j in range(n):
                length = self.dfs(matrix, i, j, dp)
                longest = max(length, longest)
        return longest

    def dfs(self, matrix, i, j, dp):
        if dp[i][j] != 0:
            return dp[i][j]
        m = len(matrix)
        n = len(matrix[0])
        length = 1
        dirs = [(0, -1), (0, 1), (-1, 0), [1, 0]]
        for d in dirs:
            dx = i + d[0]
            dy = j + d[1]
            if 0 <= dx < m and 0 <= dy < n and matrix[dx][dy] > matrix[i][j]:
                path = self.dfs(matrix, dx, dy, dp)
                #  记得 path + 1，额外加上i, j的统计
                length = max(path + 1, length)
        # 计算完成对dp[i][j]赋值
        dp[i][j] = length
        return length
