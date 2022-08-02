from typing import List


class Solution:
    def mergeSort(self, nums: List[int], tmp: List[int], l: int, r: int) -> int:
        if l >= r:
            return 0
        mid = (r + l) // 2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                inv_count += j - (mid + 1)
                tmp[pos] = nums[i]
                i += 1
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += j - (mid + 1)
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l: r + 1] = tmp[l:r + 1]
        return inv_count

    def reverse_pairs(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)
