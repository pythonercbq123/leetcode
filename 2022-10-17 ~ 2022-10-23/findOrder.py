from typing import List
from collections import defaultdict
from collections import deque


class Solution:
    def find_order(self, courses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        topological sort
        first  find the indegree == 0, add it to queue,
        remove it, and the edges with it starts.
        run it util complete.
        when the graph empty or with no v degree == 0
        :param courses:
        :param prerequisites:
        :return:
        """
        # first build graph
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            in_degree[pre[0]] += 1
        queue = deque()
        # find the degree == 0
        for k in range(courses):
            if in_degree[k] == 0:
                queue.append(k)
        in_order = []
        # 广度优先算法遍历
        while queue:
            course = queue.popleft()
            in_order.append(course)
            for c in graph[course]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    queue.append(c)
        return in_order if len(in_order) == courses else []


if __name__ == '__main__':

    s = Solution()
    ret = s.find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    print(ret)