from typing import List


class Solution:
    def min_cost_climb_stairs(self, cost: List[int]) -> int:
        # dp[i]表示从i级台阶往上爬的最小成本
        n = len(cost)
        if n <= 2:
            return min(cost)
        dp = [0] * 2
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            # dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
            dp[i % 2] = min(dp[(i - 1) % 2], dp[(i - 2) % 2]) + cost[i]
        # return min(dp[n - 1], dp[n - 2])
        return min(dp[0], dp[1])


if __name__ == '__main__':
    s = Solution()
    ret = s.min_cost_climb_stairs([1, 100, 1, 1, 100, 1])
    print(ret)
