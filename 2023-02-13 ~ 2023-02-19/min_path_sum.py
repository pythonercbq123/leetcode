from typing import List


class Solution:
    def min_path_sum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        # for i in range(1, m):
        #     dp[0][i] = grid[0][i] + dp[0][i - 1]
        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j - 1]

        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]

    def min_path_sum_one_dimension(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0 for _ in range(n)]
        dp[0] = grid[0][0]

        for j in range(1, n):
            dp[j] = grid[0][j] + dp[j - 1]

        for i in range(1, m):
            dp[0] = grid[i][0] + dp[0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[n - 1]


if __name__ == '__main__':
    s = Solution()
    ret = s.min_path_sum([[1, 3, 1], [2, 5, 2], [3, 4, 1]])
    print(ret)
    ret = s.min_path_sum_one_dimension([[1, 3, 1], [2, 5, 2], [3, 4, 1]])
    print(ret)