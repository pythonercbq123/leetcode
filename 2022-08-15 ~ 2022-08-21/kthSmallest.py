from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check_mid(mid):
            i = n - 1
            j = 0
            num = 0
            while i >= 0 and j <= n - 1:
                if matrix[i][j] <= mid:
                    # here add i+1
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left = matrix[0][0]
        right = matrix[-1][-1]
        # why not left <= right
        while left < right:

            mid = left + (right - left) // 2
            if check_mid(mid):
                right = mid
            else:
                left = mid + 1

        return left
