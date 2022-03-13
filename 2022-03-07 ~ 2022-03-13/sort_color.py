# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 必须在不使用库的sort函数的情况下解决这个问题。
# 示例 1：
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
# 示例 2：
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
# 提示：
# n == nums.length
# 1 <= n <= 300
# nums[i] 为 0、1 或 2
# 进阶：
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            while i <= right and nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            i += 1
        print(nums)


if __name__ == '__main__':
    s = Solution()
    s.sortColors([2, 2, 1, 0, 2, 1, 0, 0])

