from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(nums, path, result):
            result.append(path)
            for i in range(len(nums)):
                dfs(nums[i + 1:], path + [nums[i]], result)

        dfs(nums, [], result)
        return result

    def subset2(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(nums, index, subset, result):
            if index == len(nums):
                result.append(list(subset))
                return
            else:
                if index < len(nums):
                    dfs(nums, index + 1, subset, result)
                    subset.append(nums[index])
                    dfs(nums, index + 1, subset, result)
                    subset.pop()
        dfs(nums, 0, [], result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))
    print(s.subset2([1, 2, 3]))