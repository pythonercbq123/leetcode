from typing import List, Tuple


class Solution:
    def find_redundant_connect(self, edges: List[List[int]]) -> List[int]:
        max_vex = 0
        for edge in edges:
            max_vex = max(edge[0], edge[1], max_vex)
        fathers = [0] * (max_vex + 1)
        for i in range(1, max_vex + 1):
            fathers[i] = i
        for edge in edges:
            if not self.union(fathers, edge[0], edge[1]):
                return edge
        return []

    def union(self, fathers, i, j):
        father_i = self.find_father(fathers, i)
        father_j = self.find_father(fathers, j)
        if father_i != father_j:
            fathers[father_i] = father_j
            return True
        return False

    def find_father(self, fathers, i):
        if fathers[i] != i:
            fathers[i] = self.find_father(fathers, fathers[i])
        return fathers[i]


if __name__ == '__main__':
    s = Solution()
    ret = s.find_redundant_connect([[1, 2], [1, 3], [2, 4], [3, 4], [2, 5]])
    print(ret)
