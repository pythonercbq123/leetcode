from typing import List


class Solution:
    def combination_sum(self, nums: List, target: int):
        result = []
        self.helper(nums, target, 0, [], result)
        return result

    def helper(self, nums: List, target: int, index: int, subset: List, result: List):
        if target == 0:
            result.append(list(subset))
        elif target > 0 and index < len(nums):
            self.helper(nums, target, index + 1, subset, result)
            subset.append(nums[index])
            self.helper(nums, target-nums[index], index, subset, result)
            subset.pop()


if __name__ == '__main__':
    s = Solution()
    ret = s.combination_sum([2, 3, 5], target=8)
    print(ret)
