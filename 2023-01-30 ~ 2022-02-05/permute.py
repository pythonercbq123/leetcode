from typing import List


class Solution:
    def permute(self, nums: List):
        result = []
        self.helper(nums, 0, result)
        return result

    def helper(self, nums: List, index: int, result: List):
        if index == len(nums):
            permute = []
            for num in nums:
                permute.append(num)
            result.append(permute)
        else:
            for j in range(index, len(nums)):
                self.swap(nums, index, j)
                self.helper(nums, index + 1, result)
                self.swap(nums, index, j)

    def swap(self, nums, i, j):
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    s = Solution()
    ret = s.permute([2, 3, 5])
    print(ret)