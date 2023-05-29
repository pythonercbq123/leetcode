from typing import List


# 使数组按非递减顺序排
class Solution:

    def totalSteps(self, nums: List[int]) -> int:
        ans, st = 0, []
        for num in nums:
            max_t = 0
            while st and st[-1][0] <= num:
                max_t = max(max_t, st.pop()[1])
            max_t = max_t + 1 if st else 0
            ans = max(ans, max_t)
            st.append((num, max_t))
        return ans


if __name__ == '__main__':
    s = Solution()
    ret = s.totalSteps([8, 5, 4, 3, 2, 1, 7, 3, 6, 11, 8, 5, 11])
    print(ret)
