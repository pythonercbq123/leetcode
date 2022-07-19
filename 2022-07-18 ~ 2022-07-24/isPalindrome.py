class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s) - 1
        left = 0
        while left < right:
            s_l = s[left].lower()
            s_r = s[right].lower()
            while not s_l.isdigit() and not s_l.isalpha() and left < right:
                left += 1
                s_l = s[left].lower()
            while not s_r.isdigit() and not s_r.isalpha() and left < right:
                right -= 1
                s_r = s[right].lower()
            if left < right:
                if s_l == s_r:
                    left += 1
                    right -= 1
                else:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    r = s.isPalindrome("A man, a plan, a canal: Panama")
    print(r)