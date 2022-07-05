from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        left, right, top, bottom = 0, cols - 1, 0, rows - 1
        rs = []
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                rs.append(matrix[top][col])
            for row in range(top + 1, bottom + 1):
                rs.append(matrix[row][right])
            if left < right and top < bottom:
                for col in range(right - 1, left - 1, -1):
                    rs.append(matrix[bottom][col])
                for row in range(bottom - 1, top, -1):
                    rs.append(matrix[row][left])
            left += 1
            top += 1
            right -= 1
            bottom -= 1
        return rs


if __name__ == '__main__':
    s = Solution()
    r = s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(r)
