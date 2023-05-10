from typing import List


class Solution:
    def largestRectangeArea(self, heights: List[int]) -> int:
        stack = [-1]
        # 设置-1为边界处理奠定基础
        max_area = 0
        for i in range(len(heights)):
            # 这里比较需要用高度比较
            while stack and stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(width * height, max_area)
            stack.append(i)
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
        return max_area


if __name__ == "__main__":
    # make a test for the class
    heights = [2, 1, 5, 6, 2, 3]
    solution = Solution()
    print(solution.largestRectangeArea(heights))   
    