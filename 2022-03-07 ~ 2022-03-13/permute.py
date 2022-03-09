# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 示例 2：
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
# 示例 3：
#
# 输入：nums = [1]
# 输出：[[1]]
# 提示：
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# nums 中的所有整数 互不相同
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        size = len(nums)
        ret = []

        def back_track(index):
            if index == size:
                ret.append(nums[:])
            else:
                for i in range(index, size):
                    nums[i], nums[index] = nums[index], nums[i]
                    back_track(index + 1)
                    nums[i], nums[index] = nums[index], nums[i]

        back_track(0)
        return ret


if __name__ == '__main__':
    s = Solution()
    c = s.permute([1, 2, 3, 4])
    print(c)
