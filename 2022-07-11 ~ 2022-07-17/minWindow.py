from typing import List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        need = defaultdict(int)
        window = defaultdict(int)
        left = 0
        right = 0
        valid = 0
        start = 0
        min_len = float('inf')
        for c in t:
            need[c] += 1
        need_size = len(need)
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while valid == need_size:
                if right - left < min_len:
                    min_len = right - left
                    start = left
                c = s[left]
                left += 1
                if c in need:
                    if need[c] == window[c]:
                        valid -= 1
                    window[c] -= 1

        return '' if min_len == float('inf') else s[start: start + min_len]


if __name__ == '__main__':
    s = Solution()
    r = s.minWindow("AA", "AA")
    print(r)
