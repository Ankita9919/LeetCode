# LeetCode 203
# Verified implementation draft

class Solution:
    def removeElements(self, head, val: int):
        dummy = ListNode(0, head)
        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
