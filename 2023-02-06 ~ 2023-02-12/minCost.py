from typing import List


class Solution:
    def min_cost(self, costs: List):
        n = len(costs)
        # dp[0][0], 第i个房子粉刷为红色需要的成本
        dp = [[0] * 2 for i in range(3)]
        # 0 1 2分别为红 蓝 绿
        dp[0][0] = costs[0][0]
        dp[1][0] = costs[0][1]
        dp[2][0] = costs[0][2]
        # % 2注意压缩空间复杂度
        for i in range(1, n):
            dp[0][i % 2] = costs[i][0] + min(dp[1][(i - 1) % 2], dp[2][(i - 1) % 2])
            dp[1][i % 2] = costs[i][1] + min(dp[0][(i - 1) % 2], dp[2][(i - 1) % 2])
            dp[2][i % 2] = costs[i][2] + min(dp[0][(i - 1) % 2], dp[1][(i - 1) % 2])
        return min(dp[0][(n - 1) % 2], dp[1][(n - 1) % 2], dp[2][(n - 1) % 2])


if __name__ == '__main__':
    s = Solution()
    ret = s.min_cost([[17, 2, 6], [15, 14, 5], [13, 3, 1]])
    print(ret)
