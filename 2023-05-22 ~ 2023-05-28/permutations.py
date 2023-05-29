from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(index):
            if index == n:
                res.append(nums[:])
            else:
                for j in range(index, n):
                    swap(index, j)
                    backtrack(index + 1)
                    swap(j, index)

        def swap(i, j):
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)

        return res


if __name__ == '__main__':
    s = Solution()
    ret = s.permute([1, 2, 3])
    print(ret)
