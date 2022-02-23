# 给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。
# 第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。
# 请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。
# 你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。
# 提示:
#
# n ==  链表中的节点数
# 0 <= n <= 104
# -106 <= Node.val <= 106

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        even_head = head.next
        even = even_head
        odd = head
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


if __name__ == '__main__':
    pre = ListNode(0)
    cur = pre
    for i in range(1, 6):
        t = ListNode(i)
        cur.next = t
        cur = cur.next
    a = Solution()
    r = a.oddEvenList(pre.next)
    print(r)
