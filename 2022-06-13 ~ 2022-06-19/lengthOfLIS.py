from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        定义dp[i]是以nums[i]结尾的最长子序列长度
        :param nums:
        :return:
        """
        n = len(nums)
        if n < 1:
            return 0
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        res = 0
        for i in range(n):
            res = max(res, dp[i])
        return res

    def lengthOfLIS2(self, nums: List[int]) -> int:
        top = [0] * len(nums)
        piles = 0
        for i in range(len(nums)):
            poker = nums[i]
            left = 0
            right = piles - 1
            while left <= right:
                mid = left + (right - left) // 2
                if top[mid] > poker:
                    right = mid - 1
                elif top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid - 1
            if left == piles:
                piles += 1
            top[left] = poker
        return piles


if __name__ == '__main__':
    s = Solution()
    r = s.lengthOfLIS2([0,1,0,3,2,3])
    print(r)
