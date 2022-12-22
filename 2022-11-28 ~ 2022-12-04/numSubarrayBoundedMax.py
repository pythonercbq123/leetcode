from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List, left: int, right: int) -> int:
        """
        子数组的最大值范围在[left, right], 求这样的子数组的个数
        :param nums:
        :param left:
        :param right:
        :return:
        """
        res = 0
        last1 = last2 = -1
        for i, x in enumerate(nums):
            if left <= x <= right:
                last1 = i
            elif x > right:
                last2 = i
                last1 = -1
            if last1 != -1:
                res += last1 - last2
        return res


if __name__ == '__main__':
    s = Solution()
    ret = s.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3)
    print(ret)
