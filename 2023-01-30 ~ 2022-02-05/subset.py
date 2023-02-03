from typing import List


class Solution:
    def subset(self, nums: List):
        result = []
        if not nums:
            return result
        self.helper(nums, 0, [], result)
        return result

    def helper(self, nums: List, index: int, subset: List, result: List):
        if index == len(nums):
            # 注意这里一定需要重新生成subset, python中元素保存的是指向每个元素的地址.
            result.append(list(subset))
        else:
            self.helper(nums, index + 1, subset, result)
            subset.append(nums[index])
            self.helper(nums, index + 1, subset, result)
            subset.pop()


if __name__ == '__main__':
    s = Solution()
    ret = s.subset([1, 2, 3])
    print(ret)
