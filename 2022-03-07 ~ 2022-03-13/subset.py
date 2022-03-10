from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        size = len(nums)
        s = []

        def dfs(index, nums):
            if index == size:
                ret.append(s[:])
                return
            s.append(nums[index])
            dfs(index + 1, nums)
            s.pop()
            dfs(index + 1, nums)

        dfs(0, nums)
        return ret


if __name__ == '__main__':
    s = Solution()
    ret = s.subsets([1, 2, 3])
    print(ret)
