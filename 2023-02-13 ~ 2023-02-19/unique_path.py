from typing import List


class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(2)]
        for i in range(2):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i % 2][j] = dp[(i - 1) % 2][j] + dp[i % 2][j - 1]
        return dp[(m - 1) % 2][n - 1]

    def unique_paths_one_dimension(self, m: int, n: int) -> int:
        #  进一步压缩空间复杂度
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]
        return dp[n - 1]


if __name__ == '__main__':
    s = Solution()
    ret = s.unique_paths_one_dimension(3, 3)
    print(ret)
