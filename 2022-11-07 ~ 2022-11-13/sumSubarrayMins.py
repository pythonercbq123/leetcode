from typing import List
import math

mod = math.pow(10, 9) + 7


class Solution:
    def sum_sub_array_min(self, arr: List[int]) -> int:
        n = len(arr)
        mono_stack = []
        left = [0] * n
        right = [0] * n
        for i, x in enumerate(arr):
            while mono_stack and arr[mono_stack[-1]] >= arr[i]:
                mono_stack.pop()
            left[i] = i - (mono_stack[-1] if mono_stack else -1)
            mono_stack.append(i)
        mono_stack = []
        for i in range(n - 1, -1, -1):
            while mono_stack and arr[mono_stack[-1]] > arr[i]:
                mono_stack.pop()
            right[i] = (mono_stack[-1] if mono_stack else n) - i
            mono_stack.append(i)
        ans = 0
        for l, r, x in zip(left, right, arr):
            ans = (ans + l * r * x) % mod
        return ans


if __name__ == '__main__':
    s = Solution()
    ret = s.sum_sub_array_min([3, 1, 2, 4])
    print(ret)
