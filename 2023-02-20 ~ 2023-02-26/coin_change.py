from typing import List


class Solution:
    def coin_change(self, coins: List, target: int) -> int:
        """
        dp[i][j]表示通过前i个coin, 生成和为j的最小硬币个数
        :param coins:
        :param target:
        :return:
        """
        dp = [target + 1] * (target + 1)
        dp[0] = 0
        for coin in coins:
            for j in range(target, 0, -1):
                for k in range(1, j // coin + 1, 1):
                    dp[j] = min(dp[j - k * coin] + k, dp[j])
        return dp[target] if dp[target] < target + 1 else -1

    def coin_change_other(self, coins: List, target: int) -> int:
        """
        dp[i] 表示凑成金额为i 所需要的硬币的最小个数
        :param coins:
        :param target:
        :return:
        """
        dp = [0] * (target + 1)
        for i in range(1, target + 1):
            # 这一步非常关键
            dp[i] = target + 1
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[target]


if __name__ == '__main__':
    s = Solution()
    ret = s.coin_change([1, 2, 5], 13)
    print(ret)
    ret = s.coin_change_other([1, 2, 5], 13)
    print(ret)
