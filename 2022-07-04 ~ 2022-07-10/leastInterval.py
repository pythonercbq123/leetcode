from typing import List


class Solution:
    def leastInterval(self, tasks: List[int], n: int) -> int:
        from collections import Counter
        c = Counter(tasks)
        max_exec = max(c.values())
        max_count = sum(1 for i in c.values() if i == max_exec)
        return max((max_exec - 1) * (n + 1) + max_count, len(tasks))


if __name__ == '__main__':
    s = Solution()
    r = s.leastInterval(["A", "A", "A", "B", "B", "B"], 2)
    print(r)
