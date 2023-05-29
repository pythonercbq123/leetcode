from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        def get_height(i):
            if i < 0 or i >= len(height):
                return 0
            else:
                return height[i]

        stack = []
        n = len(height)
        area = 0
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                pop_index = stack.pop()
                if stack:
                    left = stack[-1]
                else:
                    break
                right = i
                h = min(height[left], height[right]) - height[pop_index]
                width = right - left - 1
                area += h * width
            stack.append(i)
        return area

    def d_trap(self, height):
        n = len(height)
        left_max = [height[0]] + [0] * (n - 1)
        right_max = [0] * (n - 1) + [height[n - 1]]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        ans = 0
        for i in range(n):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans


if __name__ == '__main__':
    s = Solution()
    ret = s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(ret)
    ret = s.d_trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(ret)
