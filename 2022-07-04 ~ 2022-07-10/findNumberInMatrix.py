from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m > 0:
            n = len(matrix[0])
        else:
            return False
        y = n - 1
        x = 0
        while y >= 0 and x < m:
            if matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1
            else:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    r = s.findNumberIn2DArray([[1, 1]], 0)
    print(r)