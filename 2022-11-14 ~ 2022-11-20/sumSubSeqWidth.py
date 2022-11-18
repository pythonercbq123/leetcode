from typing import List


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        """
        转化为计算每个数作为最小值和最大值的个数问题
        :param nums:
        :return:
        """
        res = 0
        mod = int(1e9 + 7)
        nums.sort()
        n = len(nums)
        pow_list = [1]
        for i in range(1, n):
            pow_list.append(pow_list[-1] * 2)
        for i in range(n):
            res = (pow_list[i] * nums[i] - pow_list[n-i-1] * nums[i] + res) % mod

        return (res + mod) % mod
