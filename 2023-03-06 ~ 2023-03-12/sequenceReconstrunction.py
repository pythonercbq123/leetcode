from typing import List
from collections import deque


class Solution:
    def seq_reconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        """
        本质是判断有向图的拓扑排序是否唯一
        题目要求org中num 1 <= num <= n
        :param org:
        :param seqs:
        :return:
        """
        graph = dict()
        in_degree = dict()
        for seq in seqs:
            for num in seq:
                if num < 1 or num > len(org):
                    return False
                graph.setdefault(num, set())
                in_degree.setdefault(num, 0)
            for i in range(len(seq) - 1):
                num_f = seq[i]
                num_b = seq[i + 1]
                if num_b not in graph[num_f]:
                    graph[num_f].add(num_b)
                    in_degree[num_b] += 1
        q = deque()
        for key in in_degree:
            if in_degree[key] == 0:
                q.append(key)
        built = []
        while len(q) == 1:
            # 此处q.popleft的命名按照q中实际内容命名即可
            num = q.popleft()
            built.append(num)
            for v in graph[num]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        return org == built


if __name__ == '__main__':
    s = Solution()
    ret = s.seq_reconstruction([4, 1, 5, 2, 6, 3], [[4, 1, 5, 2], [5, 2, 6, 3]])
    print(ret)
    ret = s.seq_reconstruction([1, 2, 3], [[1, 2], [1, 3]])
    print(ret)
