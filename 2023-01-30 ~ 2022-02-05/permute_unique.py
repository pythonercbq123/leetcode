from typing import List


class Solution:
    def permute_unique(self, nums: List) -> List:
        result = []
        self.helper(nums, 0, result)
        return result

    def helper(self, nums: List, index: int, result: List):
        if index == len(nums):
            permutation = []
            for num in nums:
                permutation.append(num)
            result.append(permutation)
        else:
            h_set = set()
            for k in range(index, len(nums)):
                if nums[k] not in h_set:
                    h_set.add(nums[k])
                    self.swap(nums, index, k)
                    self.helper(nums, index + 1, result)
                    self.swap(nums, index, k)

    def swap(self, nums, i, j):
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    s = Solution()
    ret = s.permute_unique([1, 2, 1])
    print(ret)
