from typing import List


class Solution:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        mid = self.binary_serach(nums, target)
        if mid < 0:
            return [-1, -1]
        else:
            left_bound, right_bound = mid, mid
            while left_bound >= 0 and nums[left_bound] == target:
                left_bound -= 1
            while right_bound <= len(nums) - 1 and nums[right_bound] == target:
                right_bound += 1
            return [left_bound + 1, right_bound - 1]

    def binary_serach(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    r = s.search_range(nums=[1], target=1)
    print(r)
