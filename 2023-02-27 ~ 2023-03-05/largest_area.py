from typing import List


class Solution:
    def permutation_sum(self, nums: List[int], target: int) -> int:
        """
        找出一个数组满足和为target的组合数目
        dp[i]定义为和为i的满足条件的排列数。
        :param nums:
        :param target:
        :return:
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]


if __name__ == '__main__':
    s = Solution()
    ret = s.permutation_sum([2, 1, 3], 3)
    print(ret)