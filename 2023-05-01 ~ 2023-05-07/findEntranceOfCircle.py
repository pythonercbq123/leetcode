class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# 一个链表中可能有环，找到环的起始节点
# 思路：快慢指针，快指针一次走两步，慢指针一次走一步，相遇后，快指针回到起点，快慢指针都一次走一步，再次相遇的节点就是环的起始节点
# 证明：设环的起始节点到相遇节点的距离为x，相遇节点到环的起始节点的距离为y，环的长度为r，快指针走过的距离为f，慢指针走过的距离为s
# 则有：f = 2s，f = s + nr，s = x + y，f = x + y + mr，其中n和m为正整数
# 由f = 2s和f = x + y + mr得：x + y + mr = 2(x + y)，即x + y = mr
# 由s = x + y和x + y = mr得：s = (m - 1)r + r - x，即s = (m - 1)r + (r - x)
# 由s = (m - 1)r + (r - x)和s = x + y得：x = (m - 1)r + (r - x) - y，即x = (m - 1)r + (r - x) - (r - x)，即x = (m - 1)r
# 由x = (m - 1)r得：x = (m - 1)r + 0，即x = (m - 1)r + mr - mr，即x = (m - 1)r + mr - (x + y)，即x = (m - 1)r + mr - s
# 由x = (m - 1)r + mr - s和s = (m - 1)r + (r - x)得：x = (m - 1)r + (r - x) - (m - 1)r - (r - x)，即x = (m - 1)r + (r - x) - (m - 1)r - (r - x)
# 即x = 0，即x = 0 + 0，即x = 0 + y - y，即x = y - y，即x = y - (x + y)，即x = y - s
# 由x = y - s和s = x + y得：x = y - (x + y) - x - y，即x = y - (x + y) - x - y
class Solution:
    def findEntranceInCircle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow, fast = head, head
        while True:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    def findEntranceInCircle2(self, head: ListNode):
        if head is None or head.next is None:
            return None
        fast = head
        slow = head
        print(id(fast))
        print(id(slow))
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
