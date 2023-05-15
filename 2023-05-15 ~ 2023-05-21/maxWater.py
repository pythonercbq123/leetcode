from typing import List


class Solution:
    # 盛水最多的容器 给定一个长度为n的数组height, 有n条垂线，第i条线的两个端点为(i, 0)和(i, height[i])
    # 找出其中的两条线 使得他们与x轴构成的容器可以容纳最多的水
    # 代码的目的是为了计算最大面积
    # 变量max_area表示最大面积
    # 变量left表示左边界
    # 变量right表示右边界
    # 双指针
    # 如果左边界的高度小于右边界的高度，则左边界向右移动
    # 否则，右边界向左移动
    # 返回最大面积

    def maxArea(self, height: List[int]) -> int:
        # 双指针
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
