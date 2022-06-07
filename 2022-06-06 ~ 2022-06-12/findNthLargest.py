from typing import List
import random


class Solution:

    def find_kth_largest(self, nums: List[int], k: int) -> int:
        def top_k_split(arr: List, low: int, high: int, k: int):
            mid = random_partition(arr, low, high)
            if mid == k - 1:
                return arr[mid]
            elif mid < k - 1:
                return top_k_split(arr, mid + 1, high, k)
            else:
                return top_k_split(arr, low, mid - 1, k)

        def partition(arr: List, low: int, high: int):
            pivot = arr[low]
            left, right = low, high
            while left < right:
                while left < right and arr[right] >= pivot:
                    right -= 1
                arr[left] = arr[right]

                while left < right and arr[left] <= pivot:
                    left += 1
                arr[right] = arr[left]
            arr[left] = pivot
            return left

        def random_partition(arr: List, low: int, high: int):
            pivot = random.randint(low, high)
            arr[low], arr[pivot] = arr[pivot], arr[low]
            return partition(arr, low, high)

        n = len(nums)
        return top_k_split(nums, 0, n - 1, n - k + 1)
