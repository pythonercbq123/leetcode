from collections import defaultdict


class Solution:
    def length_of_longest_substring(self, s: str) -> str:
        left, right = 0, 0
        n = len(s)
        counts = defaultdict(int)
        max_len = 0
        while right < n:
            c = s[right]
            counts[c] += 1
            while counts[c] == 2:
                counts[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len


if __name__ == '__main__':
    s = Solution()
    ret = s.length_of_longest_substring('asdfa')
    print(ret)
