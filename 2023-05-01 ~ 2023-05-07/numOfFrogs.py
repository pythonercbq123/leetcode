class Solution:
    def min_num_of_frogs(self, croakOfFrogs: str) -> int:
        ans = 0
        if len(croakOfFrogs) % 5 != 0:
            return -1
        d = {c: idx for idx, c in enumerate('croak')}
        cnt = [0] * 4
        num = 0
        for c in croakOfFrogs:
            idx = d[c]
            if idx == 0:
                num += 1
                cnt[idx] += 1
                ans = max(num, ans)
            else:
                pre = idx - 1
                if cnt[pre] == 0:
                    return -1
                cnt[pre] -= 1
                if idx == 4:
                    num -= 1
                else:
                    cnt[idx] += 1
        # "cccccccrrooaakk"
        if num > 0:
            return -1
        return ans