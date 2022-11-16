from typing import List


class Solution:
    """
    判断全局倒置和局部倒置数量是否相等
    全局倒置的数量： 满足如下条件的(i,j)的个数，
    对于0 <= i < j < n -1
    有 num[i] > num[j]

    局部倒置对于 0 <= i < n-1
    有 num[i] > num[i+1]
    """

    def is_equal(self, nums: List[int]) -> bool:
        """
        只需判断是否存在非局部配置
        即存在 i,j 是的 i< j -1 使得 num[i] > num[j]
        对于每个i， 判断是否存在 j(j >i+1)使得 num[i] > num[j]
        等价于 num[i] > min(num[i+2], num[i+3], ...num[n-1]
        :param nums:
        :return:
        """
        min_suf = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            if nums[i-1] > min_suf:
                return False
            min_suf = min(nums[i], min_suf)
        return True


if __name__ == '__main__':
    s = Solution()
    ret = s.is_equal([1, 2, 0])
    print(ret)
