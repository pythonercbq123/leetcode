class Solution:
    def replaceSpace(self, s: str) -> str:
        s_new = ''
        for i in s:
            if i == ' ':
                s_new += '%20'
            else:
                s_new += i
        return s_new
