from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        单调栈, 双指针, 动态规划
        :param height:
        :return:
        """
        stack = []
        n = len(height)
        ans = 0
        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                w = i - left - 1
                h = min(height[left], height[i]) - height[top]
                ans += w * h
            stack.append(i)
        return ans

    def trap_with_pointer(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left, right = 0, n - 1
        lmax, rmax = 0, 0
        while left < right:
            lmax = max(height[left], lmax)
            rmax = max(height[right], rmax)
            if lmax < rmax:
                ans += lmax - height[left]
                left += 1
            else:
                ans += rmax - height[right]
                right -= 1
        return ans




if __name__ == '__main__':
    s = Solution()
    s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
