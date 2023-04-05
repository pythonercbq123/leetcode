class Solution:
    def min_window(self, s: str, t: str) -> str:
        """"
        输入两个字符串s和t，
        请找出字符串s中包含字符串t的所有字符的最短子字符串。例如，输入的字符串s为"ADDBANCAD"，
        字符串t为"ABC"，则字符串s中包含字符'A'、'B'和'C'的最短子字符串是"BANC"。
        如果不存在符合条件的子字符串，则返回空字符串""。如果存在多个符合条件的子字符串，则返回任意一个。用python实现

        定义两个指针 left 和 right，分别表示滑动窗口的左右边界；
        用一个字典 need 来记录字符串 t 中每个字符出现的次数；
        用一个字典 window 来记录滑动窗口中每个字符出现的次数；
        用一个变量 match 记录当前滑动窗口中已经匹配的字符数；
        不断移动右指针，直到窗口中包含了 t 中所有的字符；
        移动左指针，使窗口中不包含多余的字符，直到不再满足条件；
        在移动左指针和右指针的过程中，记录最短的符合条件的子字符串；
        当右指针移动到字符串 s 的末尾时，如果没有找到符合条件的子字符串，则返回空字符串""。
        """
        need = {}
        window = {}
        match = 0
        left, right = 0, 0
        min_len = float('inf')
        for i in t:
            need[i] = need.get(i, 0) + 1
        n = len(s)
        start = 0
        while right < n:
            cr = s[right]
            if cr in need:
                window[cr] = window.get(cr, 0) + 1
                if window[cr] == need[cr]:
                    match += 1
            right += 1
            while match == len(need):
                if right - left < min_len:
                    start = left
                    min_len = right - left
                cl = s[left]
                if cl in need:
                    window[cl] -= 1
                    if window[cl] < need[cl]:
                        match -= 1
                left += 1
        return s[start: start + min_len] if min_len < float('inf') else ''


if __name__ == '__main__':
    s = Solution()
    ret = s.min_window("ADDBANCAD", "ABC")
    print(ret)
    ret = s.min_window("ADDBANCAD", "ABCE")
    print(ret)