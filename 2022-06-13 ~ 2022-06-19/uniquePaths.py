from typing import List
import numpy as np


class Solution:

    def unique_paths(self, m: int, n: int) -> int:
        dp = np.zeros((m, n))

        for i in range(0, n):
            dp[0][i] = 1
        for j in range(0, m):
            dp[j][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return int(dp[m - 1][n - 1])


if __name__ == '__main__':
    s = Solution()
    r = s.unique_paths(1, 1)
    print(r)
