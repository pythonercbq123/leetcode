from typing import List, Optional


class Solution:
    def two_sum(self, nums: List, k: int) -> Optional[tuple]:
        """
        :param nums: 递增数组
        :param k: target
        :return:
        """
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                return left, right
        return None


if __name__ == '__main__':
    s = Solution()
    ret = s.two_sum([1, 2, 3, 4, 6], 9)
    print(ret)
