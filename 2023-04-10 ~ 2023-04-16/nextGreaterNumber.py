from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def next_greater_num(self, head: Optional[ListNode]) -> list:
        ans = []
        s = []
        idx = -1
        while head:
            idx += 1
            ans.append(0)
            while s and s[-1][0] < head.val:
                ans[s[-1][1]] = head.val
                s.pop()
            s.append((head.val, idx))
            head = head.next
        return ans


if __name__ == '__main__':
    s = Solution()
    a = ListNode(7)
    b = ListNode(3)
    c = ListNode(4)
    d = ListNode(5)
    e = ListNode(8)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    ret = s.next_greater_num(a)
    print(ret)