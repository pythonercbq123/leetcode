from typing import List
from collections import deque


class Solution:
    def find_friend_groups(self, matrix: List[List[int]]) -> int:
        """
        找朋友圈的数量
        其实是寻找一个图中有几个子图。(通过广度优先算法或者并查集来解决)
        :param matrix:
        :return:
        """
        n = len(matrix)
        visited = [0] * n
        result = 0
        for i in range(n):
            if visited[i] == 0:
                self.find_circle(matrix, visited, i)
                result += 1
        return result

    def find_circle(self, matrix, visited, i):
        q = deque()
        q.append(i)
        visited[i] = 1
        while q:
            t = q.popleft()
            for friend in range(len(matrix)):
                if matrix[t][friend] == 1 and visited[friend] == 0:
                    q.append(friend)
                    visited[friend] = True


if __name__ == '__main__':
    s = Solution()
    ret = s.find_friend_groups([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    print(ret)
