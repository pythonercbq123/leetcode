from typing import List


class Solution:
    def coin_change(self, coins: List, amount: int) -> int:
        memo = dict()

        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float('INF')
            for i in coins:
                sub_problem = dp(n - i)
                if sub_problem == -1:
                    continue
                res = min(res, 1 + sub_problem)

            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return dp(amount)

    def coin_change_dp(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(0, amount+1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1





if __name__ == '__main__':
    s = Solution()
    t = s.coin_change([1, 2, 5], 11)
    print(t)
