from typing import List


class Solution:
    def longest_increasing_path(self, matrix: List[List[int]]):
        r = len(matrix)
        c = len(matrix[0])
        lengths = [[0] * c for _ in range(r)]
        longest_path = 0
        for i in range(r):
            for j in range(c):
                if lengths[i][j] == 0:
                    path = self.dfs(matrix, lengths, i, j) 
                    longest_path = max(longest_path, path)
        return longest_path

    def dfs(self, matrix, lengths, i, j):
        if lengths[i][j] != 0:
            return lengths[i][j]
        r = len(matrix)
        c = len(matrix[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        length = 1
        for dx, dy in dirs:
            nx = i + dx
            ny = j + dy
            if 0 <= nx < r and 0 <= ny < c and matrix[nx][ny] > matrix[i][j]:
                path = self.dfs(matrix, lengths, nx, ny)
                length = max(path + 1, length)
        lengths[i][j] = length
        return length


if __name__ == '__main__':
    s = Solution()
    ret = s.longest_increasing_path([[3, 4, 5], [2, 2, 8], [2, 2, 9]])
    print(ret)
