from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0] * n
        right = [0] * n
        mono_stack = []
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        mono_stack = []
        for k in range(n-1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[k]:
                mono_stack.pop()
            right[k] = mono_stack[-1] if mono_stack else n
            mono_stack.append(k)
        max_area = max((right[i] - left[i] - 1) * heights[i] for i in range(n))
        return max_area


if __name__ == '__main__':
    s = Solution()
    ret = s.largestRectangleArea([2, 1, 5, 6, 2, 3])
    print(ret)