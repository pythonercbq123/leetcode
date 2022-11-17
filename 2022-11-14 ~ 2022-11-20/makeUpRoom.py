from typing import List


class Solution:
    def makeup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0, 0, 0] for _ in range(n)]
        # dp[i][0]第i间屋子用红色的最小成本
        dp[0] = grid[0]
        for i in range(1, n):
            dp[i % 2][0] = min(dp[(i - 1) % 2][1], dp[(i - 1) % 2][2]) + grid[i][0]
            dp[i % 2][1] = min(dp[(i - 1) % 2][0], dp[(i - 1) % 2][2]) + grid[i][1]
            dp[i % 2][2] = min(dp[(i - 1) % 2][1], dp[(i - 1) % 2][0]) + grid[i][2]
        return min(dp[(n - 1) % 2][0], dp[(n - 1) % 1][1], dp[(n - 1) % 2][2])


if __name__ == '__main__':
    s = Solution()
    ret = s.makeup([[17, 2, 6], [15, 14, 5], [13, 3, 1]])
    print(ret)
