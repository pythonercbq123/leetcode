from typing import List
from collections import deque


class Solution:
    def open_lock(self, deadends: List, target: str) -> int:
        dead = set(deadends)
        visited = set()
        init = '0000'
        q1 = deque()
        q2 = deque()
        q1.append(init)
        steps = 0
        if target in dead or init in dead:
            return -1
        while q1:
            cur = q1.popleft()
            visited.add(cur)
            if cur == target:
                return steps
            neighbors = self.get_neighbors(cur)
            for neighbor in neighbors:
                if neighbor not in dead and neighbor not in visited:
                    visited.add(neighbor)
                    q2.append(neighbor)
            if not q1:
                q1 = q2
                q2 = deque()
                steps += 1
        return -1

    def get_neighbors(self, cur):
        nexts = []
        cur_list = list(cur)
        for i, c in enumerate(cur):
            # roll down
            if c == '0':
                nc = '9'
            else:
                nc = str(int(c) - 1)
            cur_list[i] = nc
            new_cur = ''.join(cur_list)
            nexts.append(new_cur)
            cur_list[i] = c
            # roll up
            if c == '9':
                nc = '0'
            else:
                nc = str(int(c) + 1)
            cur_list[i] = nc
            new_cur = ''.join(cur_list)
            nexts.append(new_cur)
            cur_list[i] = c
        return nexts


if __name__ == '__main__':
    s = Solution()
    ret = s.open_lock(['0102', '0201'], '0202')
    print(ret)
