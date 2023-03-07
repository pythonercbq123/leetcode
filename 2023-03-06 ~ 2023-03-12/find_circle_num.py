from typing import List


class Solution:
    def find_circle_num(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        fathers = [i for i in range(n)]
        # 可以这么理解 朋友圈最大数量开始是一共多少人，后面每两个人成为朋友就减去1
        count = n
        for i in range(n):
            # 注意从i+1开始
            for j in range(i + 1, n):
                if matrix[i][j] == 1 and self.union(fathers, i, j):
                    count -= 1
        return count

    def find_father(self, fathers, i):
        if fathers[i] != i:
            fathers[i] = self.find_father(fathers, fathers[i])
        # 注意这边 路径压缩
        return fathers[i]

    def union(self, fathers, i, j):
        father_i = self.find_father(fathers, i)
        father_j = self.find_father(fathers, j)
        if father_i != father_j:
            fathers[father_i] = father_j
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    ret = s.find_circle_num([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    print(ret)
